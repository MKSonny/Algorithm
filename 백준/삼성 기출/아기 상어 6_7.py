import sys
from collections import deque


n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

q = deque()
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

shark_size = 2
flag = False
ate = 0
moved = 0

for i in range(n):
    for j in range(n):
        if l[i][j] == 9:
            q.append((i, j))
            l[i][j] = 0
            flag = True
            break
    if flag:
        break

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    min_cur = float('inf')
    temp = []
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and l[ny][nx] <= shark_size:
                    visited[ny][nx] = visited[y][x] + 1
                    if 0 < l[ny][nx] < s
                    q.append((ny, nx))

    if len(temp) > 0:
        ate += 1
    else:
        break
    temp.sort()
    temp.sort(key=lambda o: (o[0], o[1]))
    y, x = temp[0]
    moved += visited[y][x]
    l[y][x] = 0
    q.append((y, x))

    if ate == shark_size:
        shark_size += 1
        ate = 0

print(moved)