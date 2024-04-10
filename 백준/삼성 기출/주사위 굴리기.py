import sys

n, m, start_y, start_x, r = map(int, sys.stdin.readline().rstrip().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))

move_command = list(map(int, sys.stdin.readline().rstrip().split()))

test_horizontal = [4, 1, 3]
test_vertical = [2, 1, 5, 6]

def test_move_south(arr_horizontal, arr_vertical):
    arr_vertical.insert(0, arr_vertical.pop())
    arr_horizontal[1] = arr_vertical[1]
    print_dice(arr_horizontal, arr_vertical)


def test_move_north(arr_horizontal, arr_vertical):
    arr_vertical.append(arr_vertical.pop(0))
    arr_horizontal[1] = arr_vertical[1]
    print_dice(arr_horizontal, arr_vertical)


def test_move_east(arr_horizontal, arr_vertical):
    temp = arr_horizontal.pop()
    arr_horizontal.insert(0, arr_vertical.pop())
    arr_vertical.append(temp)
    arr_vertical[1] = arr_horizontal[1]
    print_dice(arr_horizontal, arr_vertical)


def test_move_west(arr_horizontal, arr_vertical):
    temp = arr_horizontal.pop(0)
    arr_horizontal.append(arr_vertical.pop())
    arr_vertical.append(temp)
    arr_vertical[1] = arr_horizontal[1]
    print_dice(arr_horizontal, arr_vertical)


def print_dice(arr_horizontal, arr_vertical):
    print(arr_horizontal)
    print(arr_vertical)
    print()


# test_move_east(test_horizontal, test_vertical)
# test_move_east(test_horizontal, test_vertical)
# test_move_east(test_horizontal, test_vertical)
# test_move_east(test_horizontal, test_vertical)


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


for move in move_command:
    if move == 1:
        moving_to = 3
        if not is_safe(start_y, start_x, moving_to):
            continue
        move_east(arr_horizontal, arr_vertical)
    elif move == 2:
        moving_to = 2
        if not is_safe(start_y, start_x, moving_to):
            continue
        move_west(arr_horizontal, arr_vertical)
    elif move == 3:
        moving_to = 0
        if not is_safe(start_y, start_x, moving_to):
            continue
        move_north(arr_horizontal, arr_vertical)
    else:
        moving_to = 1
        if not is_safe(start_y, start_x, moving_to):
            continue
        move_south(arr_horizontal, arr_vertical)

    print(arr_horizontal[1])
    start_y += dy[moving_to]
    start_x += dx[moving_to]
    '''
    주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 
    주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
    0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 
    칸에 쓰여 있는 수는 0이 된다.
    '''
    # 위의 조건식을 안 써 오답 발생
    if l[start_y][start_x] == 0:
        l[start_y][start_x] = arr_vertical[-1]
    else:
        arr_vertical[-1] = l[start_y][start_x]
        l[start_y][start_x] = 0