import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]

max_cnt = 0

'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 1 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''

# for i in board:
#     print(i)

max_cnt = 0

def bfs(y, x):
    global max_cnt

    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

    # print(cnt)
    max_cnt = max(max_cnt, cnt)

total = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            total += 1

print(total)
print(max_cnt)