import sys

n, m, h = map(int, sys.stdin.readline().split())
board = [[False] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = True # 사다리가 있는 곳

def check():
    for start in range(n):
        now = start
        for j in range(h):
            if board[j][now]: # 가로선이 오른쪽에 존재한다면
                now += 1
            # 가로선이 왼쪽에 존재한다면
            elif now > 0 and board[j][now - 1]:
                now -= 1
        if now != start:
            return False
    return True

for i in board:
    print(i)
