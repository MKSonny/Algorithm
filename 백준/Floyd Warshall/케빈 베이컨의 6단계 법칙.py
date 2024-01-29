import sys

n, m = map(int, sys.stdin.readline().split())

l = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    l[i][i] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a - 1][b - 1] = 1
    l[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

minn = float('inf')
r = 0

for idx, i in enumerate(l):
    ssum = sum(i)
    if minn > ssum:
        minn = ssum
        r = idx + 1

print(r)