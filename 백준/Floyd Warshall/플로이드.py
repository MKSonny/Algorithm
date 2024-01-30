import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    l[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if l[a - 1][b - 1] < c:
        continue
    l[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

for i in range(n):
    for j in range(n):
        if l[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(l[i][j], end=' ')
    print()