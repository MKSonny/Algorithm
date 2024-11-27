import sys
from collections import deque

gears = deque()

for _ in range(4):
    gears.append(deque(list(map(int, sys.stdin.readline().rstrip()))))

n = int(sys.stdin.readline())

how = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    how.append((a - 1, b))

# how[0] 번째에 있는 것을 회전 시킨 후
def roll(number, clock):
    # 반시계 방향
    if clock == -1:
        # 본인은 반시계 방향으로 돈다.
        check = check_gear(gears, number)
        gears[number].append(gears[number].popleft())
        # 양 옆의 다른 두 곳은 시계 방향으로 돈다.
        # 맨끝은 양쪽이 없기 때문에 한 쪽만 처리
        # check가 [0, 1]이면 오른쪽만
        # check가 [-1, 0]이면 왼쪽만
        # 왼쪽은 시계 방향
        for i in check:
            if i == 0: continue
            gears[number + i].insert(0, gears[number + i].pop())

            if 0 <= number + i - 1 < 4 and number + i - 1 != number:
                gears[number + i - 1].append(gears[number + i - 1].popleft())
            if 0 <= number + i + 1 < 4 and number + i + 1 != number:
                gears[number + i + 1].append(gears[number + i + 1].popleft())
    else:
        check = check_gear(gears, number)

        gears[number].insert(0, gears[number].pop())

        for i in check:
            if i == 0: continue
            gears[number + i].append(gears[number + i].popleft())
            # i가 1일 경우 i - 1은 0, i + 1은 2
            if 0 <= number + i - 1 < 4 and number + i - 1 != number:
                gears[number + i - 1].insert(0, gears[number + i - 1].pop())
            if 0 <= number + i + 1 < 4 and number + i + 1 != number:
                gears[number + i + 1].insert(0, gears[number + i + 1].pop())

def check_gear(gears, number):
    # gears의 각 리스트의 i번째의 반대는?
    # 10101111 1번째
    # 01111101
    # 1번쨰에서 1번째의 [2]와 닿는 곳은 2번째의 [6]
    # 같다면? -> 회전하지 않는다.
    # 순서
    # 1. 일단 명령대로 회전 시킨다
    # 2. 회전시킨 후 양 옆을 검사하고 극이 같다면 회전 시키지 않는다.
    # 3. 양옆이 아닌 곳은 이전 회전 결과에 영향을 받는다.
    # 양 옆이 아닌 곳 구별 방법?
    # 0일 경우 양옆이 아닌 곳은 [2, 3]
    # 1일 경우 양옆이 아닌 곳은 [3]
    # 2일 경우, [0]
    # 3일 경우, [1, 2]
    # 양 옆 말고 다른 곳 까지 검사 필요
    # 2번이 회전하면 1번도 회전
    # 3번이 회전하면 4번 또는 2번도 회전
    check = [0, 0]
    if number == 0:
        if gears[number][2] != gears[number + 1][6]:
            return [0, 1]
    elif number == 3:
        if gears[number][6] != gears[number - 1][2]:
            return [-1, 0]
    else:
        if gears[number][6] != gears[number - 1][2]:
            check[0] = -1
        if gears[number][2] != gears[number + 1][6]:
            check[1] = 1
    return check

for number, w in how:
    roll(number, w)

score = 0

for i in range(len(gears)):
    if gears[i][0] == 1:
        score += (2 ** i)
print(score)