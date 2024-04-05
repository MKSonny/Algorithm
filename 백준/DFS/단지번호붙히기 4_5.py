import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(l, y, x, n):
    global cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if l[ny][nx] == 1:
                cnt += 1
                l[ny][nx] = cnt
                dfs(l, ny, nx, n)

sol = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            l[i][j] = 's'
            cnt = 1
            dfs(l, i, j, n)
            sol.append(cnt)

print(len(sol))
sol.sort()

for asw in sol:
    print(asw)