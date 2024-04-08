import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if l[i][j] == 0:
                l[i][j] = 1
                make_wall(cnt + 1)
                l[i][j] = 0


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

key = []
answer = -1
def bfs():
    global answer
    cnt = 0
    d = deque()
    l2 = copy.deepcopy(l)

    for i in range(n):
        for j in range(m):
            if l2[i][j] == 2:
                d.append((i, j))

    while d:
        y, x = d.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if l2[ny][nx] == 0:
                    l2[ny][nx] = 2
                    d.append((ny, nx))

    for i in l2:
        cnt += i.count(0)
    answer = max(answer, cnt)

make_wall(0)
print(answer)