import sys


n, m = map(int, sys.stdin.readline().split())
board = []

for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x, size):
    for i in range(4):
        ny = y + dy[i] * size
        nx = x + dx[i] * size

        if (ny >= n or ny < 0 or nx >= m or nx < 0) or board[ny][nx] != '*':
            return False

    return True

my_board = [['.' for _ in range(m)] for _ in range(n)]

answer = []

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            size = 0
            while True:
                if check(i, j, size + 1):
                    size += 1
                else:
                    break

            if size > 0:
                # 1부터 size까지 다 기록
                for s in range(1, size + 1):
                    answer.append((i + 1, j + 1, s))
                    my_board[i][j] = '*'
                    for k in range(4):
                        ny = i + dy[k] * s
                        nx = j + dx[k] * s
                        my_board[ny][nx] = '*'



if my_board == board:
    print(len(answer))
    for a, b, c in answer:
        print(a, b, c)
else:
    print(-1)