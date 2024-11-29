import sys

n, m, h = map(int, sys.stdin.readline().split())
option = []

board = [[False for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = True

for i in board:
    print(i)

def check():
    # 모든 시작점에 대해서
    for start in range(n):
        now = start
        for j in range(h):
            # 가로선이 오른쪽에 존재한다면
            if board[j][now]:
                now += 1
            elif now > 0 and board[j][now - 1]:
                now -= 1
        if now != start:
            return False
    return True

def dfs(cnt, y, x):
    global answer
    if answer <= cnt:
        return
    if check():
        answer = min(answer, cnt)
    if cnt == 3:
        return
    for i in range(y, h):
        for j in range(n - 1):
            if not board[i][j]:
                board[i][j] = True
                dfs(cnt + 1, i, j + 2)
# print(check())
dfs(0, -1, 0)