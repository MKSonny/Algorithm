# 지역의 개수, 수색범위, 길의 개수
import sys

n, m, r = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

INF = float('inf')

h = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    h[i][i] = 0

for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    h[a - 1][b - 1] = c
    h[b - 1][a - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if h[i][k] + h[k][j] < h[i][j]:
                h[i][j] = h[i][k] + h[k][j]

answer = -1

for i in range(n):
    item = 0
    for j in range(n):
        if h[i][j] <= m:
            item += l[j]
    answer = max(item, answer)

print(answer)