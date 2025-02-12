import sys
from collections import Counter

T = int(sys.stdin.readline())
lo = []
ko = []

for _ in range(T):
    lo.append(list(sys.stdin.readline().rstrip()))
    ko.append(int(sys.stdin.readline()))

di = {}


lt, rt = 0, 0

def check(to, li, ori, m):
    # 1, 5, 6
    # to = []
    for i in range(len(li)):
        te = li[i:i + m]
        # print(te)
        cnt = 0
        # print('te1', te, end=' ')
        if len(te) < m:
            continue
        to.append(te[-1] - te[0] + 1)
        # to.append(''.join(ori[te[0]:te[-1] + 1]))
    # print('a', to)
    return to



for i in range(len(lo)):
    to = []
    for idx, c in enumerate(lo[i]):
        if c not in di.keys():
            di[c] = [idx]
        else:
            di[c].append(idx)
    # print(di)
    # print(ko[], i)

    for d in di:
        if len(di[d]) >= ko[i]:
            # print(di)
            check(to, di[d], lo[i], ko[i])

    # print('to', to)
    if len(to) == 0:
        print(-1)
    else:
        print(min(to), max(to))
    di = {}
