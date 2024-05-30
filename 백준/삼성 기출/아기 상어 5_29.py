import sys
from collections import deque

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

# for i in l:
#     print(i)

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

visited = [[0 for _ in range(n)] for _ in range(n)]
ate_spot = [[False for _ in range(n)] for _ in range(n)]
baby_shark = 2
ate = 0
total_ate = 0
t = -1
def bfs(y, x, visited):
    global ate
    global baby_shark
    global ate_spot
    global total_ate
    global t
    q = deque([(y, x)])
    # cnt = 1
    while q:
        y, x = q.popleft()
        # if total_ate == 4:
        #     print('test')
        #     for i in visited:
        #         print(i)
        #     exit()
        if 0 < l[y][x] < baby_shark and not ate_spot[y][x]:
            ate += 1
            total_ate += 1
            # print(y, x)
            if ate == baby_shark:
                baby_shark += 1
                # print(y, x, baby_shark)
                ate = 0
            t = visited[y][x]
            # print(t)
            # print(t, l[y][x], y, x)
            for i in visited:
                print(i)
            print()
            # if ate == 3:
            #     break
            visited = [[0 for _ in range(n)] for _ in range(n)]
            ate_spot[y][x] = True
            # print('ate', y, x)
            visited[y][x] = t
            # q = deque([(y, x)])
            # for i in visited:
            #     print(i)
            # print()
            bfs(y, x, visited)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == 0 and l[ny][nx] <= baby_shark:
                    # cnt += 1
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
    # print('work')

for i in range(n):
    for j in range(n):
        if l[i][j] == 9:
            bfs(i, j, visited)
            break
print(t)
# print(total_ate)
# for i in visited:
#     print(i)