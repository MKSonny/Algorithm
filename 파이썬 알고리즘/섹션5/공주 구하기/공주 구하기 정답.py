import sys
from collections import deque
sys.stdin = open("in3.txt", "r")
n, k = map(int, input().split())

dq = list(range(1, n + 1))
dq = deque(dq)
cnt = 1
while len(dq) > 1:
    if cnt % k == 0:
        dq.popleft()
    else:
        dq.append(dq.popleft())
    cnt += 1

print(dq.pop())