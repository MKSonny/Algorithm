import sys
from collections import deque

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
q = []

for i in range(1, n + 1):
    q.append((i, l[i - 1]))

q = deque(q)

while True:
    idx, cnt = q.popleft()
    print(idx, end=' ')

    if len(q) == 0: break

    if cnt > 0:
        for _ in range(cnt - 1):
            q.append(q.popleft())
    else:
        cnt = cnt * -1
        for _ in range(cnt):
            q.appendleft(q.pop())
