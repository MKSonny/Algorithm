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

# print(empty)

def rowSafe(y, insert):
    for i in range(n):
        if board[y][i] == insert:
            # print('행')
            return False
    return True

def colSafe(x, insert):
    for i in range(n):
        if board[i][x] == insert:
            # print('열')
            return False
    return True

def squareSafe(x, y, insert):
    nx = x // 3 * 3
    ny = y // 3 * 3
    # (7, 4)
    # 6, 3

    for i in range(3):
        for j in range(3):
            if board[ny + i][nx + j] == insert:
                # print('사각')
                return False
    return True

def isSafe(board, insert, x, y):
    n = len(board)
    # print(insert, end=' ')
    # 행 검사
    for i in range(n):
        if board[y][i] == insert:
            # print('행')
            return False

    # 열 검사
    for i in range(n):
        if board[i][x] == insert:
            # print('열')
            return False

    nx = x // 3 * 3
    ny = y // 3 * 3
    # (7, 4)
    # 6, 3

    for i in range(3):
        for j in range(3):
             if board[ny + i][nx + j] == insert:
                 # print('사각')
                 return False
    return True

# def printBoard(board):
#     for i in range(9):
#         for j in range(9):
#             print(board[i][j], end=' ')
#         print()

# def dfs(board, level):
def dfs(level):
    # n = len(board)
    if level == len(empty):
        for i in range(n):
            print(*board[i])
        exit(0)

    print(empty)
    y = empty[level][0]
    x = empty[level][1]

    # print(y, x)

    for i in range(1, 10):
        # if isSafe(board, i, x, y):
        if rowSafe(y, i) and colSafe(x, i) and squareSafe(x, y, i):
            board[y][x] = i
            # print('insert', i)
            # board 넘겨주면 실행 속도 느려짐
            # dfs(board, level + 1)
            dfs(level + 1)
            board[y][x] = 0

dfs(0)