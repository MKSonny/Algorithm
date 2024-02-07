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
total = sum(l)

def dfs(summ, level, tsum):
    global maxx
    if summ + total - tsum < maxx:
        return
    if summ > c:
        return
    if level == n:
        maxx = max(summ, maxx)
        return
    dfs(summ + l[level], level + 1, tsum + l[level])
    dfs(summ, level + 1, tsum + l[level])


dfs(0, 0, 0)
print(maxx)