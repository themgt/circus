from collections import defaultdict
import zmq
import json
from itertools import chain
import os
import errno

from zmq.eventloop import ioloop, zmqstream

from circus.commands import get_commands
from circus.client import CircusClient
from circus.stats.collector import StatsCollector
from circus.stats.publisher import StatsPublisher
from circus import logger


class StatsStreamer(object):
    def __init__(self, endpoint, pubsub_endoint, stats_endpoint, delay=1.):
        self.topic = 'watcher.'
        self.delay = delay
        self.ctx = zmq.Context()
        self.pubsub_endpoint = pubsub_endoint
        self.sub_socket = self.ctx.socket(zmq.SUB)
        self.sub_socket.setsockopt(zmq.SUBSCRIBE, self.topic)
        self.sub_socket.connect(self.pubsub_endpoint)
        self.loop = ioloop.IOLoop()  # events coming from circusd
        self.substream = zmqstream.ZMQStream(self.sub_socket, self.loop)
        self.substream.on_recv(self.handle_recv)
        self.client = CircusClient(context=self.ctx, endpoint=endpoint)
        self.cmds = get_commands()
        self._pids = defaultdict(list)
        self._callbacks = dict()
        self.collector = StatsCollector()
        self.publisher = StatsPublisher(stats_endpoint, self.ctx)
        self.running = False  # should the streamer be running?
        self.stopped = False  # did the collect started yet?
        self.circus_pids = {}

    def publish_stats(self, watcher=None):
        """Get and publish the stats for the given watcher"""
        logger.debug('Publishing stats about {0}'.format(watcher))
        process_name = None
        for watcher, pid, stats in self.collector.collect_stats(
                watcher, self.get_pids(watcher)):
            if watcher == 'circus':
                if pid in self.circus_pids:
                    process_name = self.circus_pids[pid]

            self.publisher.publish(watcher, process_name, pid, stats)

    def get_watchers(self):
        return self._pids.keys()

    def get_pids(self, watcher=None):
        if watcher is not None:
            if watcher == 'circus':
                return self.circus_pids.keys()
            return self._pids[watcher]
        return chain(self._pid.values())

    def get_circus_pids(self):
        # getting the circusd pid
        res = self.client.send_message('dstats')
        return {os.getpid(): 'circusd-stats',
                res['info']['pid']: 'circusd'}

    def _init(self):
        self.circus_pids = self.get_circus_pids()
        if 'circus' not in self._callbacks:
            self._callbacks['circus'] = ioloop.PeriodicCallback(
                    lambda: self.publish_stats("circus"),
                    self.delay * 1000, self.loop)
        self._callbacks['circus'].start()
        self._pids.clear()
        # getting the initial list of watchers/pids
        res = self.client.send_message('list')

        for watcher in res['watchers']:
            pids = self.client.send_message('listpids', name=watcher)['pids']
            for pid in pids:
                self.append_pid(watcher, pid)

    def remove_pid(self, watcher, pid):
        if pid in self._pids[watcher]:
            logger.debug('Removing %d from %s' % (pid, watcher))
            self._pids[watcher].remove(pid)
            if len(self._pids[watcher]) == 0:
                logger.debug('Stopping the periodic callback for {0}'\
                             .format(watcher))
                self._callbacks[watcher].stop()

    def append_pid(self, watcher, pid):
        if watcher not in self._pids or len(self._pids[watcher]) == 0:
            if watcher not in self._callbacks:
                self._callbacks[watcher] = ioloop.PeriodicCallback(
                        lambda: self.publish_stats(watcher),
                        self.delay * 1000, self.loop)
            logger.debug('Starting the periodic callback for {0}'\
                         .format(watcher))
            self._callbacks[watcher].start()

        if pid in self._pids[watcher]:
            return
        self._pids[watcher].append(pid)
        logger.debug('Adding %d in %s' % (pid, watcher))

    def start(self):
        self.running = True
        logger.info('Starting the stats streamer')
        self._init()
        logger.debug('Initial list is ' + str(self._pids))
        logger.debug('Now looping to get circusd events')

        while self.running:
            try:
                self.loop.start()
            except zmq.ZMQError as e:
                logger.debug(str(e))

                if e.errno == errno.EINTR:
                    continue
                elif e.errno == zmq.ETERM:
                    break
                else:
                    logger.debug("got an unexpected error %s (%s)", str(e),
                                 e.errno)
                    raise
            else:
                break
        self.stop()

    def handle_recv(self, data):
        """called each time circusd sends an event"""
        # maintains a periodic callback to compute mem and cpu consumption for
        # each pid.
        logger.debug('Received an event from circusd: %s' % data)

        topic, msg = data
        try:
            __, watcher, action = topic.split('.')
            msg = json.loads(msg)
            if action == 'start' or (action != 'start' and self.stopped):
                self._init()

            if action in ('reap', 'kill'):
                # a process was reaped
                pid = msg['process_pid']
                self.remove_pid(watcher, pid)
            elif action == 'spawn':
                pid = msg['process_pid']
                self.append_pid(watcher, pid)
            elif action == 'start':
                self._init()
            elif action == 'stop':
                self.stop()
            else:
                logger.debug('Unknown action: %r' % action)
                logger.debug(msg)
        except Exception:
            logger.exception('Failed to handle %r' % msg)

    def stop(self):
        # stop all the periodic callbacks running
        for callback in self._callbacks.values():
            callback.stop()

        self.loop.stop()
        self.ctx.destroy(0)
        self.publisher.stop()
        self.stopped = True
        self.running = False
        logger.info('Stats streamer stopped')
