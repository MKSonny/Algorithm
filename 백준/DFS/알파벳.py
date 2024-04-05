import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input().strip()))

visited = [False] * 26
visited[ord(l[0][0] - 65)] = True


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, mark, sol):
    global maxx
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] not in mark:
                mark.add(l[ny][nx])
                # visited[ny][nx] = True
                maxx += 1
                dfs(ny, nx, mark, sol)
                mark.remove(l[ny][nx])
                sol.append(maxx)
                maxx -= 1
                # visited[ny][nx] = False


sol = []
for i in range(n):
    for j in range(m):
        if l[i][j] not in mark:
            mark.add(l[i][j])
            # visited[i][j] = True
            maxx = 1
            dfs(i, j, mark, sol)

print(max(sol))