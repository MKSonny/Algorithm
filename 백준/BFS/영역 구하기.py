from collections import deque
import sys

a, b, c = map(int, sys.stdin.readline().split())
l = [[0 for _ in range(b)] for _ in range(a)]

for _ in range(c):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            l[i][j] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cnt = 0
h = []

def bfs(ty, tx, h):
    q = deque()
    q.append((ty, tx))
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < a and 0 <= nx < b:
                if l[ny][nx] == 0:
                    q.append((ny, nx))
                    cnt += 1
                    l[ny][nx] = 1
    if cnt == 0:
        h.append(1)
    else:
        h.append(cnt)
    return 1

# for i in l:
#     print(i)

for i in range(a):
    for j in range(b):
        if l[i][j] == 0:
            cnt += bfs(i, j, h)
h.sort()
print(cnt)
for i in h:
    print(i, end=' ')