N = 4
board = [[0 for _ in range(N)] for _ in range(N)]

def isSafe(x, y, board):
    n = len(board)

    for i in range(y):
        if board[i][x] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=' ')
            else:
                print('.', end=' ')
        print()
    print()

def n_queen(board, y, n):
    if y == n:
        print_board(board)
        return

    for x in range(n):
        if isSafe(x, y, board):
            board[y][x] = 1
            n_queen(board, y + 1, n)
            board[y][x] = 0

n_queen(board, 0, N)