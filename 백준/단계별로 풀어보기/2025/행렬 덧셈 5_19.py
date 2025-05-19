import sys

n, m = map(int, sys.stdin.readline().split())

l1 = []
l2 = []

for _ in range(n):
    l1.append(list(map(int, sys.stdin.readline().split())))

for _ in range(n):
    l2.append(list(map(int, sys.stdin.readline().split())))

answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(l1[i][j] + l2[i][j], end=' ')
    print()