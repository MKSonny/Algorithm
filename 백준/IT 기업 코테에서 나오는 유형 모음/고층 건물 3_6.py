import sys
from collections import deque

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

def check_left(l, cur):
    cnt = 0
    idx = cur - 1
    flag = False

    while idx >= 0 and l[cur] > l[idx]:
        if l[cur] <= l[idx]:
            flag = True
        idx -= 1
        cnt += 1

    if not flag: return 0

    return cnt


def check_right(l, cur):
    cnt = 0
    idx = cur + 1
    flag = False

    while idx < n and l[cur] > l[idx]:
        if l[cur] <= l[idx]:
            flag = True
        idx += 1
        cnt += 1

    if not flag: return 0
    return cnt


for i in range(n):
    print(i, check_left(l, i), check_right(l, i))