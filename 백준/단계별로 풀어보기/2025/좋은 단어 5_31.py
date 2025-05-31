import sys
from collections import deque

n = int(sys.stdin.readline())
l = []

answer = 0

for _ in range(n):
    l = list(sys.stdin.readline().rstrip())

    l = deque(l)
    s = []

    while l:
        t = l.popleft()
        if s:
            if s[-1] == t:
                s.pop()
                continue
        s.append(t)

    if len(s) == 0:
        answer += 1

print(answer)