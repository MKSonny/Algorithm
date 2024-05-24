import sys

n, m = map(int, sys.stdin.readline().split())
start_y, start_x, direction = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

# 반시계 방향
# up, left, down, right
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

'''
5 5
2 2 1
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''


cnt = 0

for_d = [0, 1, 2, 3]

def dfs(y, x, d):
    global cnt

    if l[y][x] == 0:
        cnt += 1
        l[y][x] = cnt

    for i in l:
        print(i)
    print()

    for i in range(4):
        ny = y + dy[for_d[d - i]]
        nx = x + dx[for_d[d - i]]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == 0:
                # print(for_d[d - i])
                dfs(ny, nx, for_d[d - i])


    if d == 0:
        y += 1
    elif d == 1:
        x -= 1
    elif d == 2:
        y -= 1
    elif d == 3:
        x += 1

    if x < 0 or y < 0 or y >= m or x >= n:
        print(cnt)
        for i in l:
            print(i)
        exit()
    else:
        dfs(y, x, d)

dfs(start_y, start_x, direction)
'''
7 7
4 2 1
1 1 1 1 1 1 1
1 0 0 0 1 0 1
1 0 1 1 0 0 1
1 0 0 0 0 1 1
1 0 0 1 0 0 1
1 0 0 0 0 0 1
1 1 1 1 1 1 1
'''
