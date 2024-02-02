import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

cnt = 0
lt = 0
rt = 1
while lt <= rt and rt <= n:
    if rt == n:
        lt += 1
        if lt == n - 1:
            break
        rt = lt + 1
    ssum = l[lt]
    ssum += l[rt]

    if ssum == m:
        ssum -= l[rt]
        # print(lt, rt)
        rt += 1
        cnt += 1
    else:
        # print(ssum)
        ssum -= l[rt]
        rt += 1
        # print('rt', rt)

print(cnt)