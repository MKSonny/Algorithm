import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l = deque(l)
cnt = 0
robots = deque([])

while True:

    cnt += 1
    if l.count(0) == m:
        # print(l)
        break



    if l[0] <= 0:
        l.rotate()
        for i in range(len(robots)):
            if robots[i] == -1: continue
            robots[i] += 1

        continue

    l[0] -= 1
    robots.append(0) # 로봇을 올림



    l.rotate() # 벨트 이동 후
    for i in range(len(robots)):
        if robots[i] == -1: continue
        robots[i] += 1
    print(l)


    # 로봇들 한 칸 이동 가능하다면 이동
    for idx, belt_idx in enumerate(robots):
        # print(robots)
        if robots[idx] == -1:
            continue

        if belt_idx >= len(l) - 1:
            robots[idx] = -1
            continue

        if l[belt_idx + 1] > 0 and belt_idx + 1 not in robots:
            l[belt_idx + 1] -= 1
            robots[idx] += 1



    # print(l)






print(cnt)