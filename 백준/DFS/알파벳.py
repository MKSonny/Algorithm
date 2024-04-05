import sys

input = sys.stdin.readline

n, m = map(int, input().split())
l = []

for _ in range(n):
    l.append(list(input().strip()))

visited = [0] * 26
visited[ord(l[0][0]) - 65] = True

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ord(l[ny][nx]) - 65]:
                visited[ord(l[ny][nx]) - 65] = True
                dfs(ny, nx, count + 1)
                visited[ord(l[ny][nx]) - 65] = False


answer = 1
dfs(0, 0, 1)
print(answer)