def is_safe(board, x, y):
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

def dfs(board, y):
    N = len(board)

    if y == N:
        print_board(board)
        return

    for x in range(N):
        if is_safe(board, x, y):
            board[y][x] = 1
            dfs(board, y + 1)
            board[y][x] = 0

N = 4
board = [[0 for _ in range(N)] for _ in range(N)]
dfs(board, 0)