import sys
from collections import deque
from operator import truediv

n, k = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().split())
l = list(map(int, l))
l = deque(l)

robot = [0]

# 1 2 1 2 1 2
# 1 1 1 2 1 2 -> 이후 회전

# 2 1 1 1 2 1 -> 각 로봇의 위치 알아야 됨


def go_front(robot, l):
    for i in range(len(robot)):
        if robot[i] + 1 == n:
            robot[i] = -1
            continue
        if l[robot[i] + 1] > 0 and robot[i] != -1:
            l[robot[i] + 1] -= 1
            robot[i] += 1
    return robot, l


def robot_all(robot):
    for i in range(len(robot)):
        if robot[i] != -1:
            robot[i] += 1
            if robot[i] == n:
                robot[i] = -1
    return robot


def check(l):
    cnt = 0
    for i in l:
        if i == 0:
            cnt += 1
            if cnt == k:
                return True
    return False

answer = 0

while l[0] != 0:
    l.appendleft(l.pop())
    robot = robot_all(robot)
    robot, l = go_front(robot, l)
    robot.append(0)
    answer += 1
    print(l)

    if check(l):
        print(answer)
        break