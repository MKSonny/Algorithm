import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

lo = []
for _ in range(n):
    lo.append(list(map(int, sys.stdin.readline().split())))



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(y, x):
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if lo[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

for i in range(n):
    for j in range(m):
        if lo[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if lo[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for i in visited:
    print(*i)