import sys

n, m, x = map(int, sys.stdin.readline().split())
l = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    l[a].append((b, c))

for i in l:
    print(i)