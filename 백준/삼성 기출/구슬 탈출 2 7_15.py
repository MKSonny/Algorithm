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

r_visited[y][x] = True



while flag:
    print(y, x)
    print(blue_y, blue_x)
    print()
    sleep(1)
    for i in r_visited:
        print(i)
    print()
    #
    # for i in l:
    #     print(i)
    # print()

    for i in range(4):
        if l[y + dy[i]][x + dx[i]] == 'O':
            flag = False
            break
        if l[blue_y + dy[i]][blue_x + dx[i]] == 'O':
            flag = False
            print('hello world')
            break

    temp = False

    while l[y][x - 1] == '.' and not r_visited[y][x - 1]:
        x -= 1
        temp = True
        r_visited[y][x] = True

        while l[blue_y][blue_x - 1] == '.' and not b_visited[blue_y][blue_x - 1]:
            blue_x -= 1
            b_visited[blue_y][blue_x] = True

    if temp:
        answer += 1
        continue

    while l[y][x + 1] == '.' and not r_visited[y][x + 1]:
        x += 1
        temp = True
        r_visited[y][x] = True
        while l[blue_y][blue_x + 1] == '.' and not b_visited[blue_y][blue_x + 1]:
            blue_x += 1
            b_visited[blue_y][blue_x] = True

    if temp:
        answer += 1
        continue

    while l[y + 1][x] == '.' and not r_visited[y + 1][x]:
        y += 1
        temp = True
        r_visited[y][x] = True

        while l[blue_y + 1][blue_x] == '.' and not b_visited[blue_y + 1][blue_x]:
            blue_y += 1
            b_visited[blue_y][blue_x] = True

    if temp:
        answer += 1
        continue

    while l[y - 1][x] == '.' and not r_visited[y - 1][x]:
        y -= 1
        temp = True
        r_visited[y][x] = True

        while l[blue_y - 1][blue_x] == '.' and not b_visited[blue_y - 1][blue_x]:
            blue_y -= 1
            b_visited[blue_y][blue_x] = True

    if temp:
        answer += 1
        continue




print(answer)