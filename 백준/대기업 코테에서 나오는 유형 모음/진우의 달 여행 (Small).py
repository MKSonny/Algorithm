import sys

n, m = map(int, sys.stdin.readline().split())

l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

minn = float('inf')
move = [-1, 0, 1]
def dfs(l, level, minn, row, prev, total):
    if level == n:
        return min(total, minn)
    for i in move:
        if i != prev:
            if 0 <= row + i < m:
                print(l[level][row + i])
                minn = dfs(l, row + i, level + 1, minn, i, total + l[level][row + i])
                print()
    return minn

for i in range(m):
    print(dfs(l, 0, minn, i, -1, 0))

print(minn)