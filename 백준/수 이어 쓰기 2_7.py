import sys

lo = list(map(int, sys.stdin.readline().rstrip()))

te = 0
cnt = -1

for i in range(1, len(lo)):

    # te가 100을 넘어가면
    # 원래는 바로 +=10을 했지만
    # 같은게 9번정도 나와도 +=10을 하지 않는다.
    # 0 100
    # 0 101
    # 0 102
    # 0 103
    # 0 104
    # 0 105
    # 0 106
    # 0 107
    # 0 108
    # 0 109
    # 0 110

    # 0 120
    # 1 121
    # 1 122
    # 1 123
    # 2 124
    # 1 125


    # 100 101 102 103 104 105 106 107 108 109 110

    # 1 120 cnt 1
    # 9 120 cnt = 0 -> te += 10
    # 1 120

    # 1 121
    # 9 129
    # 1 131

    # 2 220
    # 2 221
    # 2 222
    # 2 223
    # 2 224
    # 2 225
    # 2 226
    # 2 227
    # 2 228
    # 2 229

    # 2 230
    # 2 231
    # 3 232

    if lo[i] <= lo[i - 1]:
        if str(lo[i]) in list(str(te))[:-1] and cnt < 10:
            cnt += 1
            print(cnt)
            continue
        else:
            cnt = -1
            te += 10


print(te, cnt)