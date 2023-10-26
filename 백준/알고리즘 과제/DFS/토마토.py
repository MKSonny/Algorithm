# left, right, down, up
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
# 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)
cnt = 0
def dfs_V2(y, x):
    global cnt
    if y < 0:
        cnt += 1
    if (0 <= x < m) and (0 <= y < n):
        if matrix[y][x] == 1 or matrix[y][x] == 0:
            matrix[y][x] = -1
            dfs_V2(y - 1, x)
            dfs_V2(y + 1, x)
            dfs_V2(y, x - 1)
            dfs_V2(y, x + 1)

dfs_cnt = 0
def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global cnt
    global dfs_cnt

    # 상,하,좌,우 확인
    for i in range(4):
        # print(x, y)
        nx = x + dx[i]
        ny = y + dy[i]

        # 갈 수 있는 갈래길의 개수를 알 수 있다.

        if (0 <= nx < m) and (0 <= ny < n) and matrix[ny][nx] == 0:
            cnt += 1
        if (0 <= nx < m) and (0 <= ny < n) and matrix[ny][nx] == 0:
            matrix[ny][nx] = -1
            dfs(ny, nx)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            dfs(i, j)
            # dfs_V2(i, j)

print(matrix)

print(cnt)
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
