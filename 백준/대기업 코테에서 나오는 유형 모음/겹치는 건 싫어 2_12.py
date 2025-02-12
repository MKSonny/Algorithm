import sys

n, k = map(int, sys.stdin.readline().split())
lo = list(map(int, sys.stdin.readline().split()))

'''
12 3
0 1 2 3 4 5 6
3 2 5 5 5 5 4 1 7 1 2 5
'''
idx = 0
cnt = 0
di = {}
di2 = {}
maxx = 1

while idx < n:
    if lo[idx] not in di.keys():
        di[lo[idx]] = 1
        di2[lo[idx]] = idx
    else:
        di[lo[idx]] += 1

    if di[lo[idx]] > k:
        cnt = 1
        # print('idx', idx)
        a = di2[lo[idx]]
        di2[lo[idx]] = a + 1
        idx = a + 1

        di = {lo[idx]: 1}
    else:
        cnt += 1

    # print(di)
    maxx = max(maxx, cnt)
    idx += 1

print(maxx)