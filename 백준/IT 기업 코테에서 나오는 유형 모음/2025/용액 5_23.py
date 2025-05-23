import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

lt, rt, t_rt = 0, len(l) - 1, len(l) - 1
min_diff = float('inf')
prev = float('inf')
min_lt, min_rt = 0, 0


while lt < rt:
    diff = abs(l[lt] + l[rt])

    if diff < min_diff:
        min_diff = diff
        min_lt = lt
        min_rt = rt
    else:
        lt += 1
        prev = float('inf')
        t_rt -= 1
        rt = t_rt
        continue

    prev = diff
    rt -= 1


print(min(l[min_lt], l[min_rt]), max(l[min_lt], l[min_rt]))