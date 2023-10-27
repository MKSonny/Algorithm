from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
zero_cnt = 0
in_zero = 0
q = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))
        elif matrix[i][j] == 0:
            in_zero += 1

while q:
    zero_cnt += len(q)
    for _ in range(len(q)):
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                q.append((ny, nx))

    cnt += 1

if zero_cnt != in_zero:
    cnt = -1

print(cnt)