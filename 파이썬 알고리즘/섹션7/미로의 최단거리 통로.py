from collections import deque

l = []

for _ in range(7):
    l.append(list(map(int, input().split())))

dis = [[0 for _ in range(7)] for _ in range(7)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dQ = deque()

dQ.append((0, 0))

cnt = 0

'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0
'''

flag = False

while dQ:
    now = dQ.popleft()

    if now[0] == 6 and now[1] == 6:
        print(dis[6][6])
        flag = True
        break

    for i in range(4):
        ny = now[0] + dy[i]
        nx = now[1] + dx[i]

        if 0 <= ny < 7 and 0 <= nx < 7:
            if l[ny][nx] == 0:
                dQ.append((ny, nx))
                dis[ny][nx] = dis[now[0]][now[1]] + 1
                l[ny][nx] = 1

if flag == False:
    print(-1)