import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0

lt, rt = 0, 1

while rt <= n and lt <= rt:
    ssum = sum(l[lt:rt])
    # print(lt, rt, ssum)
    if ssum == m:
        cnt += 1
        rt += 1
    elif ssum < m:
        rt += 1
    else:
        lt += 1

print(cnt)