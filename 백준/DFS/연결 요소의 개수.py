import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
l = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

cnt = 0

def dfs(n):
    for k in l[n]:
        if not visited[k]:
            visited[k] = True
            dfs(k)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)