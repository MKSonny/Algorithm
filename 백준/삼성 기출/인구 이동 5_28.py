import copy
import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

t_cnt = -1

def bfs(y, x, visited):
    global for_end
    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 1
    total = arr[y][x]

    while q:
        y, x = q.popleft()

        for o in range(4):
            ny_t = y + dy[o]
            nx_t = x + dx[o]
            if 0 <= ny_t < n and 0 <= nx_t < n:
                if not visited[ny_t][nx_t] and l <= abs(arr[y][x] - arr[ny_t][nx_t]) <= r:
                    cnt += 1
                    total += arr[ny_t][nx_t]
                    visited[ny_t][nx_t] = True
                    q.append((ny_t, nx_t))

    if cnt == 1:
        for_end += 1
        visited[y][x] = 2
        return

    q = deque([(y, x)])
    p = total // cnt
    arr[y][x] = p
    visited[y][x] = 2

    while q:
        y, x = q.popleft()
        for o in range(4):
            ny_t = y + dy[o]
            nx_t = x + dx[o]
            if 0 <= ny_t < n and 0 <= nx_t < n:
                if visited[ny_t][nx_t] == True:
                    visited[ny_t][nx_t] = 2

                    arr[ny_t][nx_t] = p
                    q.append((ny_t, nx_t))

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    t_cnt += 1
    for_end = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j, visited)

    if for_end == n * n:
        break

print(t_cnt)