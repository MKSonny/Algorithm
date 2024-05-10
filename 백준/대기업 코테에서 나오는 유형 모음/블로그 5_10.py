import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
'''
5 1
0 0 1 0 0
'''
maxx = -1
cnt = 0
stack = deque()
total = 0
for i in range(n):
    total += l[i]
    stack.append(l[i])
    if len(stack) > m:
        item = stack.popleft()
        total -= item
    if len(stack) == m:
        if maxx <= total:
            # cnt += 1
            maxx = total
        # maxx = max(total, maxx)

cnt = 0
stack = deque()
total = 0
for i in range(n):
    total += l[i]
    stack.append(l[i])
    if len(stack) > m:
        item = stack.popleft()
        total -= item
    if len(stack) == m:
        if maxx == total:
            cnt += 1

if maxx == 0:
    print("SAD")
else:
    print(maxx)
    print(cnt)