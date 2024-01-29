import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if l[i][j] == 0:
            l[i][j] = float('inf')

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
            print(1, end=' ')
    print()