import sys

n, m, t = map(int, sys.stdin.readline().split())
room = []

for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def spread(y, x, ori):
    s = ori // 5

    cnt = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if room[ny][nx] >= 0:
                room[ny][nx] += s
                cnt += 1


    room[y][x] -= s * cnt


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

def step_1():
    for i in range(n):
        for j in range(m):
            if room[i][j] == -1:
                air.append((i, j))
            if room[i][j] >= 5:
                temp.append((i, j, room[i][j]))

    for y, x, ori in temp:
        # y, x = temp.pop()
        spread(y, x, ori)

def step_2():
    first_y, first_x = air[0]
    # second = air[1]

    # room[0][0] = room[1][0]
    # room[first_y - 1][n - 1] = room[first_y][n - 1]

    for i in range(1, m):
        # i = 1
        # 0, 1

        # i = 2
        # 1, 2
        room[0][i - 1] = room[0][i]

    for i in range(m - 2, 0, -1):
        print('i', i)
        room[first_y][i + 1] = room[first_y][i]

    # 0, first_y

'''
0 0 1 8 6
0 1 1 8 6

1 2 3 0 0
1 2 3 3 0
'''

for _ in range(t):
    step_1()
    step_2()

for i in room:
    print(i)