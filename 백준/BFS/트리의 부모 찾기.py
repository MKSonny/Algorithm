import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())

l = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

def dfs(level):
    # level = 1
    # i = 6, 4
    # (2)
    # level = 6
    # i = 1, 3
    for i in l[level]:
        # visited[6] == 0
        # visited[6] = 1(level)
        # level은 부모를 의미
        # i는 연결된 자식을 의미
        # dfs(i) 자식으로 즉, 아래로 내려감
        # dfs(6)

        if visited[i] == 0:
            visited[i] = level
            dfs(i)

dfs(1)
for i in range(2, n + 1):
    print(visited[i])