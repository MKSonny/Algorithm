import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = [i for i in range(1, n + 1)]
q = deque(q)

# 1 2 3 4 5 6 7
# 1 2 4 5 6 7
# 1 2 4 5 7

cnt = 0
t = []
answer = []

while True:
    # print(q, t)
    if len(q) == 0:
        break
    # if len(q) == 1:
    #     print(q.popleft())
    #     break
    a = q.popleft()
    cnt += 1
    if cnt == k:
        answer.append(a)
        cnt = 0
        q.extend(t)
        t.clear()
        continue
    if len(q) == 0:
        t.append(a)
        q.extend(t)
        t.clear()
        continue

    t.append(a)

print('<', end='')
for i in range(len(answer) - 1):
    print(answer[i], end=', ')
print(str(answer[-1]) + '>')