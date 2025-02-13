import sys

n = int(sys.stdin.readline())
data = [0] + [int(sys.stdin.readline()) for _ in range(n)]

# print(data)
result = []

def dfs(v, i):
    visited[v] = True
    w = data[v]
    if not visited[w]:
        dfs(w, i)
    elif visited[w] and w == i:
        result.append(w)


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(result))
result.sort()
for i in result: print(i)