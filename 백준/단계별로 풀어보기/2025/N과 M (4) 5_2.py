import sys
from time import sleep

n, m = map(int, sys.stdin.readline().split())

p = []

def dfs(level):
    if len(p) == m:
        print(' '.join(map(str, p)))
        return

    for i in range(level, n + 1):
        p.append(i)
        dfs(i)
        p.pop()


dfs(1)