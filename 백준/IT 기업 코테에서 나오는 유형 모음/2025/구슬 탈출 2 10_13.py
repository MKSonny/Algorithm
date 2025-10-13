'''
#####
#..B#
#.#.#
#RO.#
#####
'''
import sys

n, m = map(int, sys.stdin.readline().split())
l = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def temp(y, x, option, flag):
    print(option)

    while 0 <= y < n and 0 <= x < m and l[y][x] == '.':
        y += dy[option]
        x += dx[option]
        l[y][x] = '#'

        if l[y][x] == 'O' or flag:
            flag = True
            break

    y -= dy[option]
    x -= dx[option]
    l[y][x] = '.'

    if flag:
        return

    for i in range(4):
        if i != option:
            temp(y, x, i, flag)


for _ in range(n):
    l.append(list(sys.stdin.readline().rstrip()))


ry, rx, = 0, 0


for i in range(n):
    for j in range(m):
        if l[i][j] == 'R':
            ry, rx = i, j
            break


for i in range(4):
    temp(ry, rx, i, False)



for i in l:
    print(i)