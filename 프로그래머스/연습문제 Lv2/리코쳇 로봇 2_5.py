from collections import deque


def solution(board):
    answer = 0
    n, m = len(board), len(board[0])

    di = [[9999999 for _ in range(m)] for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(n):
        board[i] = list(board[i])

    def bfs(y, x):
        q = deque([(y, x, 0)])

        while q:
            y, x, cnt = q.popleft()

            if board[y][x] == 'G':
                return cnt

            for i in range(4):
                ny = y
                nx = x
                while 0 <= ny + dy[i] < n and 0 <= nx + dx[i] < m and board[ny + dy[i]][nx + dx[i]] != 'D':
                    ny += dy[i]
                    nx += dx[i]
                if di[ny][nx] > cnt + 1:
                    di[ny][nx] = cnt + 1
                    q.append((ny, nx, cnt + 1))

        return -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                return bfs(i, j)

    return answer