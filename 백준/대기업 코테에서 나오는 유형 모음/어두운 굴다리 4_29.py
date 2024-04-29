import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().rstrip().split()))

min_i = -1

for i in range(n + 1, 1, -1):
    for key in range(m):
        s = k[key] - i
        e = k[key] + i
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
        min_i = i
    else:
        break

print(min_i)