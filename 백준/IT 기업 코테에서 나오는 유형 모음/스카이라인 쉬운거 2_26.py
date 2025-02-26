import sys
from collections import deque

n = int(sys.stdin.readline())
loc = deque([0])
max_height = -1
max_width = -1

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    loc.append(b)
loc.append(0)

# loc = deque([0, 2, 3, 1, 0])
first = loc.popleft()

answer = 0
cnt = 0

while loc:
    h = loc.popleft()
    if h < first:
        answer += cnt
        cnt = 0
    else:
        # print(h)
        cnt += 1
    first = h

print(answer)