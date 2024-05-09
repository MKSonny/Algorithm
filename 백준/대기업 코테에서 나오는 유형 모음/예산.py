import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

lt = 0
rt = max(l)
maxx = -1

while rt >= lt:
    mid = (lt + rt) // 2
    total = 0
    for i in l:
        if i <= mid:
            total += i
        else:
            total += mid
    if total > m:
        rt = mid - 1
    else:
        maxx = max(maxx, mid)
        lt = mid + 1


print(maxx)