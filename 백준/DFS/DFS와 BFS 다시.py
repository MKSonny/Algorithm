import queue
import sys

n, m, starting = map(int, sys.stdin.readline().split())

node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    node[start].append(end)
    node[end].append(start)

for i in node:
    i.sort()

# print(node)
# 3 1 4 2 5

def bfs(s):
    q = queue.Queue()
    q.put(s)
    print(s, end=' ')
    visited[s] = True

    while not q.empty():
        n = node[q.get()]
        for i in n:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                q.put(i)

def dfs(s):
    visited[s] = True
    print(s, end=' ')

    for n in node[s]:
        if not visited[n]:
            visited[n] = True
            dfs(n)

dfs(starting)
visited = [False] * (n + 1)
print()
bfs(starting)