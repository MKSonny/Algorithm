import sys

n = 9
board = []
empty = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            empty.append((i, j))

def rowSafe(y, insert):
    for i in range(n):
        if board[y][i] == insert:
            return False
    return True

def colSafe(x, insert):
    for i in range(n):
        if board[i][x] == insert:
            return False
    return True

def squareSafe(x, y, insert):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if board[ny + i][nx + j] == insert:
                # print('사각')
                return False
    return True

def dfs(level):
    if level == len(empty):
        for i in range(n):
            print(*board[i])
        exit(0)


    for i in range(1, 10):
        y = empty[level][0]
        x = empty[level][1]
        if rowSafe(y, i) and colSafe(x, i) and squareSafe(x, y, i):
            board[y][x] = i
            dfs(level + 1)
            board[y][x] = 0

dfs(0)