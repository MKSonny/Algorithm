board = [[0 for _ in range(4)] for _ in range(4)]

def isSafe(board, x, y):
    for i in range(y):
        if board[i][x] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(y - 1, -1, -1), range(x + 1, 4)):
        if board[i][j] == 1:
            return False

    return True

def queen(board, y):
    if y == len(board):
        for i in board:
            print(i)
        print()
        return

    for x in range(4):
        if isSafe(board, x, y):
            board[y][x] = 1
            queen(board, y + 1)
            board[y][x] = 0

    #return

queen(board, 0)
