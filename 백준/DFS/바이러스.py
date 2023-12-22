import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    node[start].append(end)
    node[end].append(start)

# for i in node:
#     print(i)

cnt = 0

def dfs(starting):
    global cnt
    visited[starting] = True
    for key in node[starting]:
        if not visited[key]:
            cnt += 1
            visited[key] = True
            dfs(key)

dfs(1)
print(cnt)