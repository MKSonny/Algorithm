import sys

n, k = map(int, input().split())
l = [i for i in range(1, n + 1)]

cnt = 0

def dfs(l, sol, k):
    global cnt
    if len(sol) == k:
        cnt += 1
        print(*sol)
        return
    for i in range(n):
        sol.append(l[i])
        dfs(l, sol, k)
        sol.pop()

dfs(l, [], k)
print(cnt)