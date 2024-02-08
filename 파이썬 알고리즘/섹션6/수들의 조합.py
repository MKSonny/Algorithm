n, m = map(int, input().split())
l = list(map(int, input().split()))
k = int(input())

cnt = 0

def dfs(l, m, sol, level):
    global cnt
    if len(sol) == m:
        if sum(sol) % k == 0:
            cnt += 1
        return
    for i in range(level, n):
        sol.append(l[i])
        dfs(l, m, sol, i + 1)
        sol.pop()

dfs(l, m, [], 0)
print(cnt)