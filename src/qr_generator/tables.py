from . import types

# alphanumeric characters are not encoded with unicode and instead use a special table
_ALPHANUMERIC_CHARACTER_TABLE = {
    " ": 36, "$": 37, "%": 38,
    "*": 39, "+": 40, "-": 41,
    ".": 42, "/": 43, ":": 44
}
for i in range(ord("0"), ord("9") + 1):
    _ALPHANUMERIC_CHARACTER_TABLE[chr(i)] = i - ord("0")
for i in range(ord("A"), ord("Z") + 1):
    _ALPHANUMERIC_CHARACTER_TABLE[chr(i)] = (i - ord("A")) + 10

# bits use in character count indicator
_NUMERIC_CHARACTER_COUNT_BITS = [10, 12, 14]
_ALPHANUMERIC_CHARACTER_COUNT_BITS = [9, 11, 13]
_BYTE_CHARCTER_COUNT_BITS = [8, 16, 16]

# log and antilog tables
_LOG_TABLE = [1,2,4,8,16,32,64,128,29,58,116,232,205,135,19,38,76,152,45,90,180,117,234,201,143,3,6,12,24,48,96,192,157,39,78,156,37,74,148,53,106,212,181,119,238,193,159,35,70,140,5,10,20,40,80,160,93,186,105,210,185,111,222,161,95,190,97,194,153,47,94,188,101,202,137,15,30,60,120,240,253,231,211,187,107,214,177,127,254,225,223,163,91,182,113,226,217,175,67,134,17,34,68,136,13,26,52,104,208,189,103,206,129,31,62,124,248,237,199,147,59,118,236,197,151,51,102,204,133,23,46,92,184,109,218,169,79,158,33,66,132,21,42,84,168,77,154,41,82,164,85,170,73,146,57,114,228,213,183,115,230,209,191,99,198,145,63,126,252,229,215,179,123,246,241,255,227,219,171,75,150,49,98,196,149,55,110,220,165,87,174,65,130,25,50,100,200,141,7,14,28,56,112,224,221,167,83,166,81,162,89,178,121,242,249,239,195,155,43,86,172,69,138,9,18,36,72,144,61,122,244,245,247,243,251,235,203,139,11,22,44,88,176,125,250,233,207,131,27,54,108,216,173,71,142,1]
_ANTILOG_TABLE = [None,0,1,25,2,50,26,198,3,223,51,238,27,104,199,75,4,100,224,14,52,141,239,129,28,193,105,248,200,8,76,113,5,138,101,47,225,36,15,33,53,147,142,218,240,18,130,69,29,181,194,125,106,39,249,185,201,154,9,120,77,228,114,166,6,191,139,98,102,221,48,253,226,152,37,179,16,145,34,136,54,208,148,206,143,150,219,189,241,210,19,92,131,56,70,64,30,66,182,163,195,72,126,110,107,58,40,84,250,133,186,61,202,94,155,159,10,21,121,43,78,212,229,172,115,243,167,87,7,112,192,247,140,128,99,13,103,74,222,237,49,197,254,24,227,165,153,119,38,184,180,124,17,68,146,217,35,32,137,46,55,63,209,91,149,188,207,205,144,135,151,178,220,252,190,97,242,86,211,171,20,42,93,158,132,60,57,83,71,109,65,162,31,45,67,216,183,123,164,118,196,23,73,236,127,12,111,246,108,161,59,82,41,157,85,170,251,96,134,177,187,204,62,90,203,89,95,176,156,169,160,81,11,245,22,235,122,117,44,215,79,174,213,233,230,231,173,232,116,214,244,234,168,80,88,175]

# character capacities table
_CHARACTER_CAPACITIES_TABLE = {
    1: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 41, types.Mode.ALPHANUMERIC: 25, types.Mode.BYTE: 17 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 34, types.Mode.ALPHANUMERIC: 20, types.Mode.BYTE: 14 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 27, types.Mode.ALPHANUMERIC: 16, types.Mode.BYTE: 11 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 17, types.Mode.ALPHANUMERIC: 10, types.Mode.BYTE: 7 },
    },
    2: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 77, types.Mode.ALPHANUMERIC: 47, types.Mode.BYTE: 32 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 63, types.Mode.ALPHANUMERIC: 38, types.Mode.BYTE: 26 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 48, types.Mode.ALPHANUMERIC: 29, types.Mode.BYTE: 20 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 34, types.Mode.ALPHANUMERIC: 20, types.Mode.BYTE: 14 },
    },
    3: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 127, types.Mode.ALPHANUMERIC: 77, types.Mode.BYTE: 53 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 101, types.Mode.ALPHANUMERIC: 61, types.Mode.BYTE: 42 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 77, types.Mode.ALPHANUMERIC: 47, types.Mode.BYTE: 32 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 58, types.Mode.ALPHANUMERIC: 35, types.Mode.BYTE: 24 },
    },
    4: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 187, types.Mode.ALPHANUMERIC: 114, types.Mode.BYTE: 78 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 149, types.Mode.ALPHANUMERIC: 90, types.Mode.BYTE: 62 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 111, types.Mode.ALPHANUMERIC: 67, types.Mode.BYTE: 46 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 82, types.Mode.ALPHANUMERIC: 50, types.Mode.BYTE: 34 },
    },
    5: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 255, types.Mode.ALPHANUMERIC: 154, types.Mode.BYTE: 106 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 202, types.Mode.ALPHANUMERIC: 122, types.Mode.BYTE: 84 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 144, types.Mode.ALPHANUMERIC: 87, types.Mode.BYTE: 60 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 106, types.Mode.ALPHANUMERIC: 64, types.Mode.BYTE: 44 },
    },
    6: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 322, types.Mode.ALPHANUMERIC: 195, types.Mode.BYTE: 134 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 255, types.Mode.ALPHANUMERIC: 154, types.Mode.BYTE: 106 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 178, types.Mode.ALPHANUMERIC: 108, types.Mode.BYTE: 74 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 139, types.Mode.ALPHANUMERIC: 84, types.Mode.BYTE: 58 },
    },
    7: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 370, types.Mode.ALPHANUMERIC: 224, types.Mode.BYTE: 154 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 293, types.Mode.ALPHANUMERIC: 178, types.Mode.BYTE: 122 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 207, types.Mode.ALPHANUMERIC: 125, types.Mode.BYTE: 86 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 154, types.Mode.ALPHANUMERIC: 93, types.Mode.BYTE: 64 },
    },
    8: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 461, types.Mode.ALPHANUMERIC: 279, types.Mode.BYTE: 192 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 365, types.Mode.ALPHANUMERIC: 221, types.Mode.BYTE: 152 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 259, types.Mode.ALPHANUMERIC: 157, types.Mode.BYTE: 108 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 202, types.Mode.ALPHANUMERIC: 122, types.Mode.BYTE: 84 },
    },
    9: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 552, types.Mode.ALPHANUMERIC: 335, types.Mode.BYTE: 230 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 432, types.Mode.ALPHANUMERIC: 262, types.Mode.BYTE: 180 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 312, types.Mode.ALPHANUMERIC: 189, types.Mode.BYTE: 130 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 235, types.Mode.ALPHANUMERIC: 143, types.Mode.BYTE: 98 },
    },
    10: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 652, types.Mode.ALPHANUMERIC: 395, types.Mode.BYTE: 271 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 513, types.Mode.ALPHANUMERIC: 311, types.Mode.BYTE: 213 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 364, types.Mode.ALPHANUMERIC: 221, types.Mode.BYTE: 151 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 288, types.Mode.ALPHANUMERIC: 174, types.Mode.BYTE: 119 },
    },
    11: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 772, types.Mode.ALPHANUMERIC: 468, types.Mode.BYTE: 321 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 604, types.Mode.ALPHANUMERIC: 366, types.Mode.BYTE: 251 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 427, types.Mode.ALPHANUMERIC: 259, types.Mode.BYTE: 177 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 331, types.Mode.ALPHANUMERIC: 200, types.Mode.BYTE: 137 },
    },
    12: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 883, types.Mode.ALPHANUMERIC: 535, types.Mode.BYTE: 367 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 691, types.Mode.ALPHANUMERIC: 419, types.Mode.BYTE: 287 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 489, types.Mode.ALPHANUMERIC: 296, types.Mode.BYTE: 203 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 374, types.Mode.ALPHANUMERIC: 227, types.Mode.BYTE: 155 },
    },
    13: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1022, types.Mode.ALPHANUMERIC: 619, types.Mode.BYTE: 425 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 796, types.Mode.ALPHANUMERIC: 483, types.Mode.BYTE: 331 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 580, types.Mode.ALPHANUMERIC: 352, types.Mode.BYTE: 241 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 427, types.Mode.ALPHANUMERIC: 259, types.Mode.BYTE: 177 },
    },
    14: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1101, types.Mode.ALPHANUMERIC: 667, types.Mode.BYTE: 458 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 871, types.Mode.ALPHANUMERIC: 528, types.Mode.BYTE: 362 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 621, types.Mode.ALPHANUMERIC: 376, types.Mode.BYTE: 258 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 468, types.Mode.ALPHANUMERIC: 283, types.Mode.BYTE: 194 },
    },
    15: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1250, types.Mode.ALPHANUMERIC: 758, types.Mode.BYTE: 520 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 991, types.Mode.ALPHANUMERIC: 600, types.Mode.BYTE: 412 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 703, types.Mode.ALPHANUMERIC: 426, types.Mode.BYTE: 292 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 530, types.Mode.ALPHANUMERIC: 321, types.Mode.BYTE: 220 },
    },
    16: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1408, types.Mode.ALPHANUMERIC: 854, types.Mode.BYTE: 586 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1082, types.Mode.ALPHANUMERIC: 656, types.Mode.BYTE: 450 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 775, types.Mode.ALPHANUMERIC: 470, types.Mode.BYTE: 322 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 602, types.Mode.ALPHANUMERIC: 365, types.Mode.BYTE: 250 },
    },
    17: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1548, types.Mode.ALPHANUMERIC: 938, types.Mode.BYTE: 644 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1212, types.Mode.ALPHANUMERIC: 734, types.Mode.BYTE: 504 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 876, types.Mode.ALPHANUMERIC: 531, types.Mode.BYTE: 364 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 674, types.Mode.ALPHANUMERIC: 408, types.Mode.BYTE: 280 },
    },
    18: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1725, types.Mode.ALPHANUMERIC: 1046, types.Mode.BYTE: 718 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1346, types.Mode.ALPHANUMERIC: 816, types.Mode.BYTE: 560 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 948, types.Mode.ALPHANUMERIC: 574, types.Mode.BYTE: 394 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 746, types.Mode.ALPHANUMERIC: 452, types.Mode.BYTE: 310 },
    },
    19: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 1903, types.Mode.ALPHANUMERIC: 1153, types.Mode.BYTE: 792 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1500, types.Mode.ALPHANUMERIC: 909, types.Mode.BYTE: 624 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1063, types.Mode.ALPHANUMERIC: 644, types.Mode.BYTE: 442 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 813, types.Mode.ALPHANUMERIC: 493, types.Mode.BYTE: 338 },
    },
    20: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 2061, types.Mode.ALPHANUMERIC: 1249, types.Mode.BYTE: 858 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1600, types.Mode.ALPHANUMERIC: 970, types.Mode.BYTE: 666 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1159, types.Mode.ALPHANUMERIC: 702, types.Mode.BYTE: 482 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 919, types.Mode.ALPHANUMERIC: 557, types.Mode.BYTE: 382 },
    },
    21: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 2232, types.Mode.ALPHANUMERIC: 1352, types.Mode.BYTE: 929 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1708, types.Mode.ALPHANUMERIC: 1035, types.Mode.BYTE: 711 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1224, types.Mode.ALPHANUMERIC: 742, types.Mode.BYTE: 509 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 969, types.Mode.ALPHANUMERIC: 587, types.Mode.BYTE: 403 },
    },
    22: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 2409, types.Mode.ALPHANUMERIC: 1460, types.Mode.BYTE: 1003 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 1872, types.Mode.ALPHANUMERIC: 1134, types.Mode.BYTE: 779 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1358, types.Mode.ALPHANUMERIC: 823, types.Mode.BYTE: 565 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1056, types.Mode.ALPHANUMERIC: 640, types.Mode.BYTE: 439 },
    },
    23: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 2620, types.Mode.ALPHANUMERIC: 1588, types.Mode.BYTE: 1091 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2059, types.Mode.ALPHANUMERIC: 1248, types.Mode.BYTE: 857 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1468, types.Mode.ALPHANUMERIC: 890, types.Mode.BYTE: 611 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1108, types.Mode.ALPHANUMERIC: 672, types.Mode.BYTE: 461 },
    },
    24: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 2812, types.Mode.ALPHANUMERIC: 1704, types.Mode.BYTE: 1171 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2188, types.Mode.ALPHANUMERIC: 1326, types.Mode.BYTE: 911 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1588, types.Mode.ALPHANUMERIC: 963, types.Mode.BYTE: 661 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1228, types.Mode.ALPHANUMERIC: 744, types.Mode.BYTE: 511 },
    },
    25: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 3057, types.Mode.ALPHANUMERIC: 1853, types.Mode.BYTE: 1273 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2395, types.Mode.ALPHANUMERIC: 1451, types.Mode.BYTE: 997 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1718, types.Mode.ALPHANUMERIC: 1041, types.Mode.BYTE: 715 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1286, types.Mode.ALPHANUMERIC: 779, types.Mode.BYTE: 535 },
    },
    26: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 3283, types.Mode.ALPHANUMERIC: 1990, types.Mode.BYTE: 1367 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2544, types.Mode.ALPHANUMERIC: 1542, types.Mode.BYTE: 1059 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1804, types.Mode.ALPHANUMERIC: 1094, types.Mode.BYTE: 751 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1425, types.Mode.ALPHANUMERIC: 864, types.Mode.BYTE: 593 },
    },
    27: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 3517, types.Mode.ALPHANUMERIC: 2132, types.Mode.BYTE: 1465 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2701, types.Mode.ALPHANUMERIC: 1637, types.Mode.BYTE: 1125 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 1933, types.Mode.ALPHANUMERIC: 1172, types.Mode.BYTE: 805 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1501, types.Mode.ALPHANUMERIC: 910, types.Mode.BYTE: 625 },
    },
    28: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 3669, types.Mode.ALPHANUMERIC: 2223, types.Mode.BYTE: 1528 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 2857, types.Mode.ALPHANUMERIC: 1732, types.Mode.BYTE: 1190 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2085, types.Mode.ALPHANUMERIC: 1263, types.Mode.BYTE: 868 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1581, types.Mode.ALPHANUMERIC: 958, types.Mode.BYTE: 658 },
    },
    29: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 3909, types.Mode.ALPHANUMERIC: 2369, types.Mode.BYTE: 1628 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 3035, types.Mode.ALPHANUMERIC: 1839, types.Mode.BYTE: 1264 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2181, types.Mode.ALPHANUMERIC: 1322, types.Mode.BYTE: 908 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1677, types.Mode.ALPHANUMERIC: 1016, types.Mode.BYTE: 698 },
    },
    30: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 4158, types.Mode.ALPHANUMERIC: 2520, types.Mode.BYTE: 1732 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 3289, types.Mode.ALPHANUMERIC: 1994, types.Mode.BYTE: 1370 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2358, types.Mode.ALPHANUMERIC: 1429, types.Mode.BYTE: 982 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1782, types.Mode.ALPHANUMERIC: 1080, types.Mode.BYTE: 742 },
    },
    31: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 4417, types.Mode.ALPHANUMERIC: 2677, types.Mode.BYTE: 1840 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 3486, types.Mode.ALPHANUMERIC: 2113, types.Mode.BYTE: 1452 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2473, types.Mode.ALPHANUMERIC: 1499, types.Mode.BYTE: 1030 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 1897, types.Mode.ALPHANUMERIC: 1150, types.Mode.BYTE: 790 },
    },
    32: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 4686, types.Mode.ALPHANUMERIC: 2840, types.Mode.BYTE: 1952 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 3693, types.Mode.ALPHANUMERIC: 2238, types.Mode.BYTE: 1538 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2670, types.Mode.ALPHANUMERIC: 1618, types.Mode.BYTE: 1112 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2022, types.Mode.ALPHANUMERIC: 1226, types.Mode.BYTE: 842 },
    },
    33: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 4965, types.Mode.ALPHANUMERIC: 3009, types.Mode.BYTE: 2068 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 3909, types.Mode.ALPHANUMERIC: 2369, types.Mode.BYTE: 1628 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2805, types.Mode.ALPHANUMERIC: 1700, types.Mode.BYTE: 1168 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2157, types.Mode.ALPHANUMERIC: 1307, types.Mode.BYTE: 898 },
    },
    34: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 5253, types.Mode.ALPHANUMERIC: 3183, types.Mode.BYTE: 2188 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 4134, types.Mode.ALPHANUMERIC: 2506, types.Mode.BYTE: 1722 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 2949, types.Mode.ALPHANUMERIC: 1787, types.Mode.BYTE: 1228 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2301, types.Mode.ALPHANUMERIC: 1394, types.Mode.BYTE: 958 },
    },
    35: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 5529, types.Mode.ALPHANUMERIC: 3351, types.Mode.BYTE: 2303 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 4343, types.Mode.ALPHANUMERIC: 2632, types.Mode.BYTE: 1809 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3081, types.Mode.ALPHANUMERIC: 1867, types.Mode.BYTE: 1283 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2361, types.Mode.ALPHANUMERIC: 1431, types.Mode.BYTE: 983 },
    },
    36: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 5836, types.Mode.ALPHANUMERIC: 3537, types.Mode.BYTE: 2431 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 4588, types.Mode.ALPHANUMERIC: 2780, types.Mode.BYTE: 1911 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3244, types.Mode.ALPHANUMERIC: 1966, types.Mode.BYTE: 1351 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2524, types.Mode.ALPHANUMERIC: 1530, types.Mode.BYTE: 1051 },
    },
    37: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 6153, types.Mode.ALPHANUMERIC: 3729, types.Mode.BYTE: 2563 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 4775, types.Mode.ALPHANUMERIC: 2894, types.Mode.BYTE: 1989 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3417, types.Mode.ALPHANUMERIC: 2071, types.Mode.BYTE: 1423 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2625, types.Mode.ALPHANUMERIC: 1591, types.Mode.BYTE: 1093 },
    },
    38: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 6479, types.Mode.ALPHANUMERIC: 3927, types.Mode.BYTE: 2699 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 5039, types.Mode.ALPHANUMERIC: 3054, types.Mode.BYTE: 2099 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3599, types.Mode.ALPHANUMERIC: 2181, types.Mode.BYTE: 1499 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2735, types.Mode.ALPHANUMERIC: 1658, types.Mode.BYTE: 1139 },
    },
    39: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 6743, types.Mode.ALPHANUMERIC: 4087, types.Mode.BYTE: 2809 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 5313, types.Mode.ALPHANUMERIC: 3220, types.Mode.BYTE: 2213 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3791, types.Mode.ALPHANUMERIC: 2298, types.Mode.BYTE: 1579 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 2927, types.Mode.ALPHANUMERIC: 1774, types.Mode.BYTE: 1219 },
    },
    40: {
        types.ErrorCorrection.L: { types.Mode.NUMERIC: 7089, types.Mode.ALPHANUMERIC: 4296, types.Mode.BYTE: 2953 },
        types.ErrorCorrection.M: { types.Mode.NUMERIC: 5596, types.Mode.ALPHANUMERIC: 3391, types.Mode.BYTE: 2331 },
        types.ErrorCorrection.Q: { types.Mode.NUMERIC: 3993, types.Mode.ALPHANUMERIC: 2420, types.Mode.BYTE: 1663 },
        types.ErrorCorrection.H: { types.Mode.NUMERIC: 3057, types.Mode.ALPHANUMERIC: 1852, types.Mode.BYTE: 1273 },
    },
}

def _get_char_count_bits(mode: 'types.Mode', version: int) -> int:
    """
    Get number of bits used to specify character count based on 
    mode and version
    """
    lookup_index = -1

    if 1 <= version and version <= 9:
        lookup_index = 0
    elif 10 <= version and version <= 26:
        lookup_index = 1
    elif 27 <= version and version <= 40:
        lookup_index = 2

    match mode:
        case types.Mode.NUMERIC:
            return _NUMERIC_CHARACTER_COUNT_BITS[lookup_index]
        case types.Mode.ALPHANUMERIC:
            return _ALPHANUMERIC_CHARACTER_COUNT_BITS[lookup_index]
        case types.Mode.BYTE:
            return _BYTE_CHARCTER_COUNT_BITS[lookup_index]
        case _:
            # this branch should be unreachable if correct types are passed into this function
            raise TypeError("Invalid mode specifier")

