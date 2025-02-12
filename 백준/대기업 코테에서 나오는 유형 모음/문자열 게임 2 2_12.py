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
    print('li', li)
    for i in range(len(li)):
        te = li[i:i + m]
        cnt = 0
        # print('te1', te, end=' ')
        if len(te) < m:
            continue
        print('te2', te)
        # c = Counter(ori[te[0]:te[-1] + 1])
        # te[0], te[-1] 사이에 'b'가 몇 개 있는지 검사 필요
        for v in c.values():
            if v >= m:
                cnt += 1
            if cnt >= 2:
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
    print(di)
    # print(ko[], i)

    for d in di:
        if len(di[d]) >= ko[i]:
            check(to, di[d], lo[i], ko[i])

    # print('to', to)
    if len(to) == 0:
        print(-1)
        continue
    print(min(to), max(to))

    di = {}