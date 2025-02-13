import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque([n])
MAX = 100001
l = [0] * MAX

while q:
    v = q.popleft()
    if v == m:
        print(l[v])
        break
    for move in (2 * v, v - 1, v + 1):
        if 0 <= move < MAX and not l[move]:
            if move == 2 * v:
                l[move] = l[v]
            else:
                l[move] = l[v] + 1
            q.append(move)