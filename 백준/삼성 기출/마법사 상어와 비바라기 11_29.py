import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

moves = []

for _ in range(m):
    moves.append(list(map(int, sys.stdin.readline().split())))

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 첫 구름 좌표
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

cross_y = [-1, 1, -1, 1]
cross_x = [-1, 1, 1, -1]

for d, s in moves:
    moved_clouds = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for y, x in clouds:
        ny = (y + dy[d - 1] * s) % n
        nx = (x + dx[d - 1] * s) % n
        board[ny][nx] += 1 # 비 내리기
        visited[ny][nx] = True
        # 이동한 구름 죄표에 추가
        moved_clouds.append((ny, nx))

    for y, x in moved_clouds:
        cnt = 0
        # 이동한 후 대각 4 방향을 조사하여 count만큼 물의 양 추가
        for d in range(4):
            ny = y + cross_y[d]
            nx = x + cross_x[d]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                cnt += 1
        board[y][x] += cnt

    new_clouds = []
    for y in range(n):
        for x in range(n):
            # 만약 이전 구름 좌표들과 겹치지 않고 2 보다 크다면
            if not visited[y][x] and board[y][x] >= 2:
                board[y][x] -= 2
                new_clouds.append((y, x))
    # clouds를 new_clouds로 교체
    clouds = new_clouds

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)