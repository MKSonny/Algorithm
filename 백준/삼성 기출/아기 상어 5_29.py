import sys
from collections import deque

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

shark_size = 2

def bfs(y, x):
    q = deque([(y, x)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    t_list = []
    visited[y][x] = 1
    dist = 0

    while q:
        y, x = q.popleft()

        if dist == visited[y][x]:
            return t_list, dist - 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and l[ny][nx] <= shark_size:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                    # 나모다 작은 물고기인 경우 먹음
                    if 0 < l[ny][nx] < shark_size:
                        t_list.append((ny, nx))
                        dist = visited[ny][nx]

    return t_list, dist - 1


for i in range(n):
    for j in range(n):
        if l[i][j] == 9:
            loc_y, loc_x = i, j
            l[i][j] = 0
            break

cnt = ans = 0

while True:
    t_list, dist = bfs(loc_y, loc_x)
    # print(t_list, dist)
    if len(t_list) == 0:
        break
    t_list.sort(key=lambda x: (x[0], x[1]))
    loc_y, loc_x = t_list[0]
    l[loc_y][loc_x] = 0
    cnt += 1
    ans += dist
    if shark_size == cnt:
        shark_size += 1
        cnt = 0

print(ans)