import sys

n = int(sys.stdin.readline())

board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, 10 + a):
        for j in range(b, 10 + b):
            board[i][j] = 1

answer = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            answer += 1

print(answer)