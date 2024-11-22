import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
start_y, start_x, direction = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(m)] for _ in range(n)]
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))


# 북, 동, 남, 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


q = deque([(start_y - 1, start_x - 1, direction)])
visited[start_y - 1][start_x - 1] = True

c = copy.deepcopy(l)

dir = [0, 1, 2, 3]
dir_idx = dir.index(direction)
dir_dict = {0: '북', 1: '동', 2: '남', 3: '서'}

# 0인 경우 북쪽,
# 1인 경우 동쪽,
# 2인 경우 남쪽,
# 3인 경우 서쪽
answer = 0
y, x = start_y - 1, start_x - 1
while True:
    # y, x, dir_idx = q.popleft()
    # 먼저 4방향 중 청소되지 않은 칸이 있는 지 확인한다.
    flag = False
    unC = False
    c[y][x] = 2
    # for i in c:
    #     print(i)
    # print()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == 0:
                # 4방향 중에서 청소되지 않은 칸이 있을 경우
                # 반시계 방향으로 90도 회전한다 (기존 방향에서 -1)
                unC = True
                break
    if unC:
        if y == 4:
            print('test', y, x, dir_idx)
            for i in c:
                print(i)
            print()
        for _ in range(4):
            dir_idx -= 1
            if dir_idx < 0:
                dir_idx += 4
                # print(y, x, dir_dict[dir_idx])

                # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진
            move_y = y + dy[dir_idx]
            move_x = x + dx[dir_idx]
            if 0 <= move_y < n and 0 <= move_x < m:
                if l[move_y][move_x] == 0 and not visited[move_y][move_x]:
                    # 한 칸 전진
                    answer += 1
                    visited[move_y][move_x] = True
                    y, x = move_y, move_x
                    flag = True
                    break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 후진하고 1번으로 돌아간다

    if flag == False:
        print(y, x, dir_idx)
        for_back = dir_idx + 2
        if for_back > 3:
            for_back -= 4
        move_y = y + dy[for_back]
        move_x = x + dx[for_back]
        if 0 <= move_y < n and 0 <= move_x < m:
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
            if l[move_y][move_x] == 1:
                break
            else:
                # if not visited[move_y][move_x]:
                #     # 바라보는 방향을 유지해야 하기 때문에 += 2를 취소
                #     visited[move_y][move_x] = True
                y, x = move_y, move_x
                # print(y, x, dir_idx)
                # q.append((move_y, move_x, dir_idx))

# for i in visited:
#     print(i)
print(answer)