
Code coverage
=============


::

    Name                            Stmts   Miss  Cover   Missing
    -------------------------------------------------------------
    /Users/tarek/Dev/github.com/circus-master/bin/bottle                       1613    878    46%   25-36, 95-96, 117, 121, 129, 133, 160-161, 164-165, 191-193, 231-233, 236, 298, 301, 310, 320-322, 334-336, 353-354, 373-374, 378-384, 403-404, 412-417, 420, 424-431, 465-468, 479, 483, 487-488, 512-514, 563-588, 597, 607-615, 622-623, 626, 631-633, 639, 643-645, 693, 697, 701, 705, 709-712, 716-719, 727-730, 740-749, 765, 776-780, 786-815, 828-829, 832-845, 892, 896, 902-904, 911-915, 923-927, 945-950, 969-973, 981-984, 1024, 1035-1036, 1057-1060, 1073, 1091-1092, 1106-1107, 1112, 1122-1126, 1134-1137, 1143-1144, 1148, 1158-1172, 1175, 1192-1193, 1196-1197, 1227-1228, 1232-1235, 1238, 1241-1242, 1247, 1257-1261, 1267-1269, 1295, 1300-1303, 1307, 1315, 1320-1321, 1324-1325, 1330, 1340, 1346-1349, 1384-1405, 1410-1412, 1415-1418, 1459-1462, 1485-1487, 1491-1494, 1504-1509, 1523, 1525-1526, 1528, 1548, 1551-1558, 1611-1613, 1621, 1625, 1649-1653, 1671, 1677-1679, 1697, 1701-1704, 1708, 1711, 1714, 1717, 1720-1724, 1745-1747, 1750-1754, 1757, 1760-1761, 1782-1784, 1787-1791, 1805, 1823-1858, 1874, 1879-1883, 1888-1895, 1901, 1906-1908, 1913-1918, 1923, 1928, 1934, 1948-1956, 1968-1987, 1995-2008, 2014-2022, 2052-2054, 2060-2061, 2114-2116, 2155-2161, 2167-2175, 2181-2183, 2194-2198, 2204-2216, 2222-2223, 2229-2231, 2237-2238, 2245-2249, 2292-2298, 2305-2312, 2332-2399, 2407-2410, 2413-2432, 2435, 2438-2440, 2453, 2473-2486, 2492-2499, 2504-2508, 2515, 2524, 2529-2537, 2540-2543, 2548-2555, 2558-2563, 2568-2578, 2581-2584, 2587-2590, 2596-2602, 2605-2615, 2627, 2637-2642, 2647-2650, 2654, 2658-2740, 2743-2746, 2749-2762, 2766-2769, 2779-2794, 2812-2822, 2909-2929
    circus/__init__                    40     29    28%   1-35, 105-117, 123
    circus/arbiter                    185     35    81%   91-105, 132-133, 160-165, 168-173, 204-205, 210, 214, 230, 234-239, 258, 274, 304, 315
    circus/client                      55      8    85%   18, 22, 50-51, 55, 63, 76-77
    circus/commands/addwatcher         24     14    42%   1-66, 73, 78
    circus/commands/base               72     53    26%   1-11, 19, 26, 35-61, 65-79, 82, 86-97, 103-106
    circus/commands/decrproc           16     14    13%   1-53, 57-60
    circus/commands/dstats             24     23     4%   1-63, 66-81
    circus/commands/get                25     19    24%   1-66, 76, 80-86
    circus/commands/globaloptions      29     21    28%   1-73, 79-81, 93-99
    circus/commands/incrproc           20     16    20%   1-51, 58-65
    circus/commands/list               23     17    26%   1-52, 61-67
    circus/commands/listpids           17     13    24%   1-41, 47-50
    circus/commands/numprocesses       19     17    11%   1-57, 59-60, 67-70
    circus/commands/numwatchers        14     13     7%   1-42, 45-48
    circus/commands/options            20     18    10%   1-101, 105-111
    circus/commands/quit                7      6    14%   1-36
    circus/commands/reload             17     15    12%   1-68, 70-71
    circus/commands/restart            15     13    13%   1-56, 58-59
    circus/commands/rmwatcher          12     10    17%   1-54
    circus/commands/sendsignal         47     33    30%   1-109, 114, 118, 124, 127, 130, 138-147
    circus/commands/set                34     22    35%   1-59, 70, 75
    circus/commands/start              15     12    20%   1-53, 58
    circus/commands/stats              49     41    16%   1-89, 93-99, 109-135
    circus/commands/status             23     20    13%   1-65, 70-80
    circus/commands/stop               12      8    33%   1-50
    circus/commands/util               54     42    22%   1-38, 43, 47, 52, 55-56, 59-60, 64
    circus/config                     137     64    53%   41-44, 56, 59-62, 73-97, 102-105, 120-132, 143-145, 148, 159, 161, 164, 167, 170, 172, 177-202
    circus/consumer                    32     10    69%   24, 28-31, 35, 38-42
    circus/controller                 116     13    89%   75, 85-86, 94-96, 104, 118, 142, 145, 151, 156-157
    circus/plugins/__init__           140    101    28%   34-43, 47-55, 59-81, 85-93, 105-108, 118-119, 131, 136, 141, 149-160, 181-247, 251
    circus/process                    123     40    67%   3-9, 97, 102, 105-125, 152, 169-170, 193-194, 198, 204, 210, 216-219, 224-229, 242-243, 247
    circus/py3compat                   47     44     6%   1-38, 43-67
    circus/sighandler                  36     16    56%   34-44, 47, 50, 53, 56, 59
    circus/sockets                     50     12    76%   38, 49-56, 65-66, 76
    circus/stats/__init__              40     27    33%   34-81, 85
    circus/stats/client               133     99    26%   28-33, 46-117, 122-128, 131, 134-137, 141-180, 184
    circus/stats/collector             30     25    17%   8-28, 31-47
    circus/stats/publisher             26     19    27%   9-14, 17-28, 31-33
    circus/stats/streamer             130    106    18%   19-37, 41-49, 52, 55-59, 63-64, 68-81, 84-90, 93-105, 108-130, 136-160, 164-172
    circus/stream/__init__             35      7    80%   16, 29, 34, 37-38, 41, 68
    circus/stream/base                 64      8    88%   22, 39, 51, 58, 65, 70, 76-77
    circus/stream/sthread              19      1    95%   25
    circus/util                       216    103    52%   1-56, 60-78, 84-86, 92, 106-113, 125, 149-150, 160-161, 165, 170-173, 177-178, 184-185, 190, 192, 202, 211, 224, 232, 244, 252, 254, 258-264, 270-275, 280-294, 307-308, 330-331
    circus/watcher                    327     78    76%   136, 164, 174, 233, 259, 263, 284, 288, 291-292, 297, 324, 340, 343-346, 375-376, 379-380, 388, 406-408, 421-423, 433-435, 441-446, 452-453, 463-464, 481, 500, 511, 520-523, 530, 533, 536-538, 542-544, 549, 553, 563, 578-579, 583, 586, 588-589, 591-592, 594-595, 597, 599-600, 604-609, 621
    circus/web/__init__                 0      0   100%   
    circus/web/circushttpd            131     76    42%   14-15, 41, 51, 60, 69, 77, 85-92, 97, 110, 118-122, 127, 153-173, 184-186, 193-209, 223, 227-232, 253-274, 278-281
    circus/web/controller             111     59    47%   10-11, 27, 44-45, 48-52, 55-56, 64-65, 68-71, 74-77, 80, 83-87, 90-92, 95-103, 111-120, 123-136
    /Users/tarek/Dev/github.com/gevent-zeromq/gevent_zeromq/core                120     41    66%   3-14, 18, 35, 57, 78, 81-83, 91-95, 99, 102, 109-116, 125, 129-135, 147-153, 161, 168, 172, 195, 199
    base_html   NoSource: No source for code: '/Users/tarek/Dev/github.com/circus-master/docs/base_html': [Errno 2] No such file or directory: '/Users/tarek/Dev/github.com/circus-master/docs/base_html'
    index_html   NoSource: No source for code: '/Users/tarek/Dev/github.com/circus-master/docs/index_html': [Errno 2] No such file or directory: '/Users/tarek/Dev/github.com/circus-master/docs/index_html'
    -------------------------------------------------------------
    TOTAL                            4544   2359    48%   


