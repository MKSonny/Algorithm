from collections import deque
import sys
input = sys.stdin.readline

# m이 x, n이 y
m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= ny < n and 0 <= nx < m:
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = matrix[y][x] + 1
                q.append((ny, nx))

ans = 0

for line in matrix:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans, max(line))

print(ans - 1)