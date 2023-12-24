import sys

input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

def isSafe(board, y, x):
    for i in range(y):
        if board[i][x] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x + 1, len(board))):
        if board[i][j] == 1:
            return False

    return True


cnt = 0

def n_queen(board, y):
    global cnt

    if y == len(board):
        cnt += 1
        return

    for x in range(len(board)):
        if isSafe(board, y, x):
            board[y][x] = 1
            n_queen(board, y + 1)
            board[y][x] = 0

n_queen(board, 0)
print(cnt)