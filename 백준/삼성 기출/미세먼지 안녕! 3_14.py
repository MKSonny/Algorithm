import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
room = []

for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

cur = []

def spread():
    while cur:
        y, x, value = cur.pop()
        count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if room[ny][nx] >= 0:
                    room[ny][nx] += value // 5
                    count += 1
        room[y][x] -= (value // 5) * count


temp = []
air = []

'''
2, 0 -> 0, 2
꼭지점 부분에 있는 먼지
0, 0 -> 1, 0 앞이 변함 +1
0, 7 -> 0, 6
2, 7 -> 1, 7 앞이 변함 -1


0번째 행에 있는 먼지는 x좌표를 -1
2번째 행에 있는 먼지는 x좌표를 +1

3, 0 -> 3, 맨 끝
'''

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def step2_ver4(a, b):
    y, x = a, 1
    index = 1
    temp = 0

    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if ny == n or nx == m or ny == -1 or nx == -1:
            index = (index - 1) % 4
            continue
        if y == a and x == 0:
            break
        '''
        2, 1, 1, 0
        temp = 0
        room[y][x] = 2
        2, 0 = 0, 2
        temp = 2
        room[y][x] = 0
        '''
        room[y][x], temp = temp, room[y][x]
        y, x = ny, nx

    y, x = b, 1
    index = 1
    temp = 0

    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if ny == n or nx == m or ny == -1 or nx == -1:
            index = (index + 1) % 4
            continue
        if y == b and x == 0:
            break

        room[y][x], temp = temp, room[y][x]
        y, x = ny, nx



'''
0 0 1 8 6
0 1 1 8 6

1 2 3 0 0
1 2 3 3 0
'''

answer = 0

for i, line in enumerate(room):
    for j, value in enumerate(line):
        if value > 0:
            cur.append((i, j, value))
        if value == -1:
            air.append((i, j))

for _ in range(t):
    spread()
    step2_ver4(air[0][0], air[1][0])
    for i, line in enumerate(room):
        for j, value in enumerate(line):
            if value > 0:
                cur.append((i, j, value))


for i in range(n):
    for j in range(m):
        if room[i][j] == -1: continue
        answer += room[i][j]

print(answer)