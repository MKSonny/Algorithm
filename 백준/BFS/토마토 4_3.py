import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

l = []

for _ in range(m):
    l.append(list(map(int, sys.stdin.readline().split())))

deq = deque()

for i in range(m):
    for j in range(n):
        if l[i][j] == 1:
            deq.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while deq:
    y, x = deq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if l[ny][nx] == 0:
                deq.append((ny, nx))
                l[ny][nx] = l[y][x] + 1

maxx = -1

for line in l:
    for tomato in line:
        maxx = max(maxx, tomato)
        if tomato == 0:
            print(-1)
            exit()

print(maxx - 1)