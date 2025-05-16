import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

q = deque([])

di = {}

for i in range(10, 36):
    di[i] = chr(i + 55)


while n:
    k = n % m
    if k >= 10:
        q.appendleft(di[k])
    else:
        q.appendleft(str(k))
    n //= m

print(''.join(q))