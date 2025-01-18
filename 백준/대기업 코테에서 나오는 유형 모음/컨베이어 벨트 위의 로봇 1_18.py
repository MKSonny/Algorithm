import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().split())
l = list(map(int, l))
l = deque(l)

answer = 0
robot = deque([False] * n)

while True:
    l.rotate(1)
    robot.rotate(1)

    robot[n - 1] = False

    for i in range(n - 2, -1, -1):
        if l[i + 1] > 0 and robot[i + 1] == False and robot[i]:
            robot[i], robot[i + 1] = False, True
            l[i + 1] -= 1

    robot[n - 1] = False

    if l[0] > 0:
        robot[0] = True
        l[0] -= 1

    answer += 1

    if l.count(0) >= k:
        break

print(answer)