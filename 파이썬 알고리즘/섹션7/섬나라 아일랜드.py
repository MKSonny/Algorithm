from collections import deque

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

def bfs(dQ):
    while dQ:
        y, x = dQ.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n:
                if l[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dQ.append((ny, nx))

dQ = deque()

cnt = 0

for y in range(n):
    for x in range(n):
        if l[y][x] == 1 and not visited[y][x]:
            dQ.append((y, x))
            visited[y][x] = True
            bfs(dQ)
            cnt += 1

print(cnt)