import sys

n = int(sys.stdin.readline())
li = []
board = []
rank = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        board.append((li[i][j], i, j))

board.sort(reverse=True)

for idx, item in enumerate(board):
    a, i, j = item
    rank[i][j] = idx + 1

for i in rank: print(i)