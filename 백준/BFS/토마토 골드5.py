import copy
import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())
k = []

for i in range(h):
    nl = []
    for j in range(m):
        nl.append(list(map(int, sys.stdin.readline().split())))
    k.append(nl)



dh = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

def bfs(q):
    while q:
        qh, y, x = q.popleft()
        for j in range(6):
            nh = qh + dh[j]
            ny = y + dy[j]
            nx = x + dx[j]
            if 0 <= nh < h and 0 <= ny < m and 0 <= nx < n:
                if k[nh][ny][nx] == 0:
                    q.append((nh, ny, nx))
                    k[nh][ny][nx] = k[qh][y][x] + 1



q = deque()

for xh in range(h):
    for i in range(m):
        for j in range(n):
            if k[xh][i][j] == 1:
                q.append((xh, i, j))

bfs(q)

maxx = -1
flag = False

for xh in range(h):
    for i in range(m):
        for j in range(n):
            if k[xh][i][j] == 0:
                flag = True
            maxx = max(maxx, k[xh][i][j])

if flag:
    print(-1)
else:
    print(maxx - 1)