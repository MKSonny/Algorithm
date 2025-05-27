import sys

n = int(sys.stdin.readline())

l = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(y, x, like):
    cnt = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] == 0:
                cnt += 1
            if board[ny][nx] in like:
                cnt += 10

    return (y, x, cnt)

board = [[0 for _ in range(n)] for _ in range(n)]

di = {}


for _ in range(n ** 2):
    l.append(list(map(int, sys.stdin.readline().split())))

def research(y, x, like):
    cnt = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] in like:
                cnt += 1

    return cnt



for me, a, b, c, d in l:

    temp = []

    di[me] = [a, b, c, d]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                y, x, cnt = check(i, j, [a, b, c, d])
                temp.append((cnt, y, x))

    temp.sort(key=lambda o:(-o[0], o[1], o[2]))
    cnt, y, x = temp[0]

    board[y][x] = me

answer = 0

for i in range(n):
    for j in range(n):
        cnt = research(i, j, di[board[i][j]])
        if cnt > 1:
            if cnt == 2:
                answer += 10
            elif cnt == 3:
                answer += 100
            else:
                answer += 1000
        else:
            answer += cnt


print(answer)