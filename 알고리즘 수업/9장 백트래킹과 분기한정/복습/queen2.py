N = 4
board = [[0 for _ in range(N)] for _ in range(N)]

def isSafe(board, x, y):
    N = len(board)
    for i in range(y):
        if board[i][x] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(y - 1, -1, -1), range(x + 1, N)):
        if board[i][j] == 1:
            return False
    return True

def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()
    print()

def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        print_board(board)
        return

    for i in range(N):
        if isSafe(board, i, y):
            board[y][i] = 1
            solve_N_Queen(board, y + 1)
            board[y][i] = 0


solve_N_Queen(board, 0)