n, m = map(int, input().split())

l = [i for i in range(1, n + 1)]
res = [0] * m
cnt = 0

def dfs(l, res, level):
    global cnt
    if level == m:
        cnt += 1
        print(*res)
        return
    for i in range(n):
        res[level] = l[i]
        dfs(l, res, level + 1)

dfs(l, res, 0)
print(cnt)