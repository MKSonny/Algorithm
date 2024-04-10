import sys

n, m, start_y, start_x, r = map(int, sys.stdin.readline().rstrip().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))

move_command = list(map(int, sys.stdin.readline().rstrip().split()))

# 주사위를 두 개의 리스트로 표현
arr_horizontal = [0, 0, 0]
arr_vertical = [0, 0, 0, 0]

def move_east(arr_horizontal, arr_vertical):
    temp = arr_horizontal.pop()
    arr_horizontal.insert(0, arr_vertical.pop())
    arr_vertical.append(temp)
    arr_vertical[1] = arr_horizontal[1]

def move_west(arr_horizontal, arr_vertical):
    temp = arr_horizontal.pop(0)
    arr_horizontal.append(arr_vertical.pop())
    arr_vertical.append(temp)
    arr_vertical[1] = arr_horizontal[1]

def move_south(arr_horizontal, arr_vertical):
    arr_vertical.insert(0, arr_vertical.pop())
    arr_horizontal[1] = arr_vertical[1]

def move_north(arr_horizontal, arr_vertical):
    arr_vertical.append(arr_vertical.pop(0))
    arr_horizontal[1] = arr_vertical[1]

# 남, 북, 서, 동
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

arr_horizontal = [0, 0, 0]
arr_vertical = [0, 0, 0, 0]
arr_vertical[-1] = l[start_y][start_x]

# 이동 방향이 지도를 벗어날 경우를 검사한다.
def is_safe(y, x, moving_to):
    ny = y + dy[moving_to]
    nx = x + dx[moving_to]

    if 0 <= nx < m and 0 <= ny < n:
        return True
    return False

cnt = 0

for move in move_command:
    y, x = start_y, start_x
    if move == 1:
        moving_to = 3
        if not is_safe(y, x, moving_to):
            continue
        move_east(arr_horizontal, arr_vertical)
    elif move == 2:
        moving_to = 2
        if not is_safe(y, x, moving_to):
            continue
        move_west(arr_horizontal, arr_vertical)
    elif move == 3:
        moving_to = 0
        if not is_safe(y, x, moving_to):
            continue
        move_north(arr_horizontal, arr_vertical)
    else:
        moving_to = 1
        if not is_safe(y, x, moving_to):
            continue
        move_south(arr_horizontal, arr_vertical)

    print(arr_horizontal[1])
    start_y += dy[moving_to]
    start_x += dx[moving_to]
    arr_vertical[-1] = l[start_y][start_x]
    cnt += 1
    print(cnt, move)
    print(arr_horizontal, arr_vertical)