import sys
from time import sleep

n, m = map(int, sys.stdin.readline().split())

p = []
idx = 1
t_idx = 1

def dfs(p, level, idx):
    if level == n:
        return

    p.append(idx)
    print(p)
    for _ in range(level, n + 1):
        dfs(p, level + 1, idx)
        idx += 1
    p.pop()
    idx = level

dfs(p, 0, 1)