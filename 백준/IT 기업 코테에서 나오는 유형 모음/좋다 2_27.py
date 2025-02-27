import sys
from collections import deque

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

# l = deque(l)
l.sort()
answer = 0

for i in range(n):
    t = l.pop(i)

    lt = 0
    rt = n - 2
    # print(t, l)

    while lt < rt:
        if l[lt] + l[rt] < t:
            lt += 1
        elif l[lt] + l[rt] == t:
            answer += 1
            break
        else:
            rt -= 1

    l.insert(i, t)

print(answer)