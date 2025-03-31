import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = [i for i in range(1, n + 1)]
q = deque(q)

cnt = 0
answer = []

while len(q):
    for _ in range(k - 1):
        q.append(q.popleft())
    answer.append(str(q.popleft()))

print('<', end='')
for i in range(n - 1):
    print(answer[i], end=', ')
print(answer[-1] + '>')