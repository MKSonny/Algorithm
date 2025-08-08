import sys

sys.setrecursionlimit(1000000)

n, m, r = map(int, sys.stdin.readline().split())

l = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    l[u].append(v)
    l[v].append(u)


for i in range(1, n + 1):
    l[i] = sorted(l[i], reverse=True)


v = [0 for _ in range(n + 1)]

level = 0

def dfs(node, visited):
    visited[node] = True
    global level
    level += 1

    v[node] = level
    for i in sorted(l[node], reverse=True):
        if not visited[i]:
            dfs(i, visited)

visited = [False for _ in range(n + 1)]
dfs(r, visited)

for i in range(1, n + 1):
    print(v[i])