n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

mark = [False] * 3

minn = float('inf')

def dfs(l, level, sol, mark):
    global minn
    if level == n:
        r = sum(sol)
        if r < minn:
            minn = r
        return
    for i in range(3):
        if not mark[i]:
            sol.append(l[level][i])
            mark = [False] * 3
            mark[i] = True
            dfs(l, level + 1, sol, mark)
            mark[i] = False
            sol.pop()

dfs(l, 0, [], mark)
print(minn)