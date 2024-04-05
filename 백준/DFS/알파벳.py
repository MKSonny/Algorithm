import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input().strip()))

visited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

mark = set()

def dfs(y, x, mark, sol):
    global maxx
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] not in mark and not visited[ny][nx]:
                mark.add(l[ny][nx])
                visited[ny][nx] = True
                maxx += 1

                dfs(ny, nx, mark, sol)
                mark.remove(l[ny][nx])
                sol.append(maxx)
                maxx -= 1
                visited[ny][nx] = False

sol = []
maxx = 1
visited[0][0] = True
mark.add(l[0][0])

dfs(0, 0, mark, sol)
# print(sol)
print(max(sol))