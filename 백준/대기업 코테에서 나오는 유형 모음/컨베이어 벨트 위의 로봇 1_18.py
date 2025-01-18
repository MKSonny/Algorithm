import sys
from collections import deque
from operator import truediv
from tabnanny import check

n, k = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().split())
l = list(map(int, l))
l = deque(l)

answer = 0
belt = deque([False] * n)

while True:
    answer += 1

    l.rotate(1)
    belt.rotate(1)

    belt[n - 1] = False

    for i in range(n - 2, -1, -1):
        if belt[i] and not belt[i + 1] and l[i + 1] > 0:
            belt[i], belt[i + 1] = False, True
            l[i + 1] -= 1

    belt[n - 1] = False

    if l[0] > 0:
        belt[0] = True
        l[0] -= 1

    if l.count(0) >= k:
        break

print(answer)