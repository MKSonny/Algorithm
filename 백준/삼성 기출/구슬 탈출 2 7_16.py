import sys
from collections import deque
from time import sleep

n, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(list(sys.stdin.readline().rstrip()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if l[i][j] == 'R':
            y, x = i, j
        if l[i][j] == 'B':
            blue_y, blue_x = i, j

answer = 0

flag = True
r_visited = [[False for _ in range(m)] for _ in range(n)]
b_visited = [[False for _ in range(m)] for _ in range(n)]


def move(x, y, dx, dy):
    cnt = 0

    while l[y + dy][x + dx] != '#' and l[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1

    return y, x, cnt