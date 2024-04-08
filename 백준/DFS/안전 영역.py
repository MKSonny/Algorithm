import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
l = []
maxx = -1

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    maxx = max(max(a), maxx)
    l.append(a)



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(visited, y, x, level):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and l[ny][nx] > level:
                visited[ny][nx] = True
                dfs(visited, ny, nx, level)

cnt = 0
answer = []

for level in range(1, maxx + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if l[i][j] > level and not visited[i][j]:
                cnt += 1
                dfs(visited, i, j, level)

    answer.append(cnt)
    cnt = 0

asw = max(answer)
if asw == 0:
    print(1)
else:
    print(asw)