import sys

n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort(reverse=True)

min_cnt = float('inf')
def dfs(l, level, sol):
    global min_cnt
    if min_cnt <= len(sol):
        return
    if sum(sol) > m:
        return
    if sum(sol) == m:
        print(sol)
        min_cnt = min(min_cnt, len(sol))
        return
    for i in range(n):
        sol.append(l[i])
        dfs(l, level + 1, sol)
        sol.pop()

dfs(l, 0, [])
print(min_cnt)