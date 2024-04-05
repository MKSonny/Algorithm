import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

cnt = -1

def dfs(n):
    global cnt
    if not visited[n]:
        visited[n] = True
        cnt += 1
        for key in l[n]:
            dfs(key)
    else:
        return

dfs(1)
# print(visited)
print(cnt)