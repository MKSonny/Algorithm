import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

lt, rt = 0, len(l) - 1
min_diff = float('inf')
min_lt, min_rt = 0, 0

while lt < rt:
    diff = l[lt] + l[rt]

    if diff == 0:
        min_lt = l[lt]
        min_rt = l[rt]
        break

    if abs(diff) < min_diff:
        min_diff = abs(diff)
        min_lt = l[lt]
        min_rt = l[rt]

    if diff < 0:
        lt += 1
    else:
        rt -= 1

print(min_lt, min_rt)