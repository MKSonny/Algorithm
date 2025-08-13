import sys

n = int(sys.stdin.readline())

l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split()))[1:])

def check(l):
    n = len(l)
    cnt = 0
    idx = 1

    while idx < n:
        if l[idx - 1] > l[idx]:
            l[idx - 1], l[idx] = l[idx], l[idx - 1]
            idx = 0
            cnt += 1
        idx += 1

    return cnt

for i in range(n):
    print(i + 1, check(l[i]))