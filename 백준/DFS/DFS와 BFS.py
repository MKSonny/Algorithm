import queue
import sys

input = sys.stdin.readline

n, m, starting = map(int, input().split())

node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    node[start].append(end)
    node[end].append(start)

for i in node:
    i.sort()

def dfs(s):
    if not visited[s]:
        visited[s] = True
        print(s, end=' ')
    for key in node[s]:
        if not visited[key]:
            visited[key] = True
            print(key, end=' ')
            dfs(key)

bfs_visited = [False] * (n + 1)

def bfs(s, bfs_visited):
    bfs_visited[s] = True
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        v = q.get()
        print(v, end = ' ')
        for key in node[v]:
            if not bfs_visited[key]:
                bfs_visited[key] = True
                q.put(key)

# visited[starting] = True
# print(starting)
dfs(starting)
print()
bfs(starting, bfs_visited)