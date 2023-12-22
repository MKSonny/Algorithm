import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

node = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    node[start].append(end)
    node[end].append(start)

# for i in node:
#     print(i)

cnt = 0

def dfs(starting):
    # global cnt
    visited[starting] = 1
    for key in node[starting]:
        if visited[key] == 0:
            # cnt += 1
            visited[key] = 1
            dfs(key)

dfs(1)
print(sum(visited) - 1)