from collections import deque


def solution(board):
    answer = 0

    for i in range(len(board)):
        board[i] = list(board[i])

    # for i in board:
    #     print(i)

    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                y, x = i, j

    q = deque([(y, x)])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    board[y][x] = 0

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        cnt = board[y][x]

        for i in range(4):
            ny = y
            nx = x

            while 0 <= ny < n and 0 <= nx < m and board[ny][nx] != 'D':
                ny += dy[i]
                nx += dx[i]

            if board[ny - dy[i]][nx - dx[i]] == 'G':
                return cnt + 1
                break

            if not visited[ny - dy[i]][nx - dx[i]]:
                board[ny - dy[i]][nx - dx[i]] = cnt + 1
                visited[ny - dy[i]][nx - dx[i]] = True
                q.append((ny - dy[i], nx - dx[i]))

    return -1