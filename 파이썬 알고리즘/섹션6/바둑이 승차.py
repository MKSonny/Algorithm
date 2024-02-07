import sys

c, n = map(int, sys.stdin.readline().split())
l = []
'''
259 5
81
58
42
33
61
'''

for _ in range(n):
    l.append(int(sys.stdin.readline()))

maxx = -1

def dfs(l, n, c, sol, level, remaining):
    global maxx
    if sum(sol) > c:
        return
    if remaining + sum(sol) < maxx:
        return
    if level == n:
        maxx = max(sum(sol), maxx)
        return
    for i in range(level, n):
        sol.append(l[i])
        dfs(l, n, c, sol, i + 1, remaining - l[i])
        sol.pop()

dfs(l, n, c, [], 0, sum(l))
print(maxx)