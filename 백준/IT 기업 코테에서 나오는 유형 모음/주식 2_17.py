import sys

t = int(sys.stdin.readline())

def dfs(n, level, li, st, total):
    if level == n:
        return

    dfs(n, level + 1, li, st.append(li[level]), total - li[level])
    for s in st:
        total += s - li[level]
    st = []
    dfs(n, level + 1, li, st, total)
    dfs(n, level + 1, li, st, total)


for _ in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    dfs(n, 0, li, [], 0)
