import sys
sys.setrecursionlimit(10**6)

n, m, r = map(int, sys.stdin.readline().split())
l = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

for i in l:
    i.sort()

record = []
cnt = 0

def dfs(node, visited):
    # visited[node] = True
    global cnt
    cnt += 1
    visited[node] = cnt

    for i in l[node]:
        if visited[i] == 0:
            dfs(i, visited)

visited = [0 for _ in range(n + 1)]

dfs(r, visited)
for i in range(1, n + 1):
    print(visited[i])
# print(visited)