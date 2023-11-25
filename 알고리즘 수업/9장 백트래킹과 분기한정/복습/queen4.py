N = 4
board = [[None for _ in range(N)] for _ in range(N)]

def isSafe(board, x, y):
    n = len(board)

    for i in range(y):
        if board[i][x] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x - 1, - 1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def printBoard(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def queen(board, y):
    if y == len(board):
        printBoard(board)
        return

    for i in range(N):
        if isSafe(board, i, y):
            board[y][i] = 1
            queen(board, y + 1)
            board[y][i] = 0

queen(board, 0)