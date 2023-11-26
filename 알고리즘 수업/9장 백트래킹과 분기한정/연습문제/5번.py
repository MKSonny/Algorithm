import copy

solution = []

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


def solve_N_Queen(board, y):
    N = len(board)
    if y == N:
        solution.append(copy.deepcopy(board))
        return

    for x in range(N):
        if isSafe(board, x, y):
            board[y][x] = 1
            solve_N_Queen(board, y + 1)
            board[y][x] = 0

n = 4
board = [[0 for _ in range(n)] for _ in range(n)]
solve_N_Queen(board, 0)

for i in solution:
    for j in i:
        print(j)
    print()