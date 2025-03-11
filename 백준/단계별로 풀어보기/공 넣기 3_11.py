import sys

n, m = map(int, sys.stdin.readline().split())
l = [0 for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    for i in range(a - 1, b):
        l[i] = c

for i in l:
    print(i, end=' ')