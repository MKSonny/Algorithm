import sys

n, m = map(int, sys.stdin.readline().split())

lo = []
for _ in range(n):
    lo.append(list(map(int, sys.stdin.readline().split())))

dir = [-1, 0, 1]
minn = float('inf')

def dfs(level, cur, prev, total):
    global minn
    total += lo[level][cur]
    if level == n - 1:
        minn = min(minn, total)
        # print()
        return
    # print(lo[level][cur])
    for i in range(3):
        if i != prev and 0 <= cur + dir[i] < m:
            dfs(level + 1, cur + dir[i], i, total)

for i in range(m):
    dfs(0, i, -1, 0)
print(minn)