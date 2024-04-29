import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().rstrip().split()))
k.sort()

min_i = -1

lt = 0
rt = n

while rt >= lt:
    mid = (lt + rt) // 2

    for key in range(m):
        s = k[key] - mid
        e = k[key] + mid

        if s < 0:
            s = 0
        if e >= n:
            e = n

        if key == 0:
            prev_s = s
            prev_e = e
        else:
            if prev_e >= s:
                prev_e = e


    if prev_s == 0 and prev_e == n:
        print(mid)
        break
    else:
        lt = mid + 1