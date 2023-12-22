import sys
sys.setrecursionlimit(10000)
cnt = 0
def dfs(x, y):
    if 0 <= x < r and 0 <= y < c:
        if field[y][x] == 1:
            # left
            field[y][x] = 0
            dfs(x, y - 1)
            # right
            dfs(x, y + 1)
            # up
            dfs(x - 1, y)
            # down
            dfs(x + 1, y)

t = int(input())

for _ in range(t):
    r, c, m = map(int, input().split())
    field = [[0 for _ in range(r)] for _ in range(c)]
    cnt = 0
    for i in range(m):
        x, y = map(int, input().split())
        field[y][x] = 1
    for i in range(r):
        for j in range(c):
            if field[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)