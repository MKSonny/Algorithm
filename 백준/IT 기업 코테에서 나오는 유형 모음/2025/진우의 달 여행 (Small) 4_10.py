import sys

n, m = map(int, sys.stdin.readline().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1]

answer = float('inf')
def dfs(y, x, prev, cnt):
    global answer

    if y == n:
        # print(cnt)
        answer = min(answer, cnt)
        cnt -= board[y - 1][x]
        return

    cnt += board[y][x]

    for i in range(3):
        if i == prev: continue
        nx = x + dx[i]
        if 0 <= nx < m:
            dfs(y + 1, nx, i, cnt)

for x in range(m):
    dfs(0, x, -1, 0)

print(answer)