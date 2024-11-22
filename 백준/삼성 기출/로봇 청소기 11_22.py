import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
y, x, direction = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(m)] for _ in range(n)]
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))


# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


visited[y][x] = True

c = copy.deepcopy(l)

dir = [0, 1, 2, 3]
dir_dict = {0: '북', 1: '동', 2: '남', 3: '서'}

# 0인 경우 북쪽,
# 1인 경우 동쪽,
# 2인 경우 남쪽,
# 3인 경우 서쪽
answer = 1
while True:
    # 먼저 4방향 중 청소되지 않은 칸이 있는 지 확인한다.
    cleaned = False
    for _ in range(4):
        direction = (direction - 1) % 4
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진
        move_y = y + dy[direction]
        move_x = x + dx[direction]
        if 0 <= move_y < n and 0 <= move_x < m and l[move_y][move_x] == 0 and not visited[move_y][move_x]:
                # 한 칸 전진
                answer += 1
                visited[move_y][move_x] = True
                y, x = move_y, move_x
                cleaned = True
                break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 후진하고 1번으로 돌아간다

    if not cleaned:
        for_back = (direction + 2) % 4
        # if for_back > 3:
        #     for_back -= 4
        move_y2 = y + dy[for_back]
        move_x2 = x + dx[for_back]
        if 0 <= move_y2 < n and 0 <= move_x2 < m and l[move_y2][move_x2] != 1:
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
            # 바라보는 방향을 유지해야 하기 때문에 += 2를 취소
            y, x = move_y2, move_x2
        else:
            break
print(answer)