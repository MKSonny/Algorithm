import sys

n, m = map(int, sys.stdin.readline().split())
start_y, start_x, direction = map(int, sys.stdin.readline().split())
l = []

visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

# 반시계 방향
# down, right, up, left
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

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

for_d = [3, 0, 1, 2]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0

def dfs(y, x, d):
    global cnt
    if l[y][x] == 0:
        cnt += 1
        # print(y, x)
        l[y][x] = cnt

    visited[y][x] += 1
    if visited[y][x] == 20:
        print(cnt)

        # for i in l:
        #     print(i)
        # print()
        #
        # for i in visited:
        #     print(i)
        # for i in l:
        #     print(i)
        exit()
    flag = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == 0:
                flag = True
                if i == for_d[d]:
                    dfs(ny, nx, for_d[d])
    if flag:
        dfs(y, x, for_d[d])

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
        exit()
    elif l[y][x] == 1:
        print(cnt)
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


# def dfs(y, x, d):
#     global cnt
#     # visited[y][x] = True
#     if visited[y][x] == 2:
#         for i in l:
#             print(i)
#         print(cnt)
#         exit()
#
#     if l[y][x] == 0:
#         # l[y][x] = cnt
#         cnt += 1
#
#     l[y][x] = 2
#     visited[y][x] += 1
#
#
#     # for i in l:
#     #     print(i)
#     # print()
#
#     for i in range(4):
#         ny = y + dy[for_d[d - i]]
#         nx = x + dx[for_d[d - i]]
#         if 0 <= ny < n and 0 <= nx < m:
#             if l[ny][nx] == 0:
#                 dfs(ny, nx, for_d[d + 1])
#
#     # for i in range(4):
#     #     ny = y + dy[for_d[d - i]]
#     #     nx = x + dx[for_d[d - i]]
#     #     if 0 <= ny < n and 0 <= nx < m:
#     #         if l[ny][nx] == 2:
#     #             dfs(ny, nx, for_d[d - i])
#             # if l[ny][nx] == 0:
#                 # print(for_d[d - i])
#
#
#     if d == 0:
#         y += 1
#     elif d == 1:
#         x -= 1
#     elif d == 2:
#         y -= 1
#     elif d == 3:
#         x += 1
#
#     if x < 0 or y < 0 or y >= m or x >= n:
#         print(cnt)
#         # for i in l:
#         #     print(i)
#         exit()
#     elif l[y][x] == 1:
#         print(cnt)
#         # for i in l:
#         #     print(i)
#         exit()
#     else:
#         dfs(y, x, d)
#
# dfs(start_y, start_x, direction)