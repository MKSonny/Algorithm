'''
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB


8x8 칸 선택 -> 검사?
0부터 시작
13 - 8 = 5
if i + 8 >= 13: break?
i = 0
0 + 8까지

i = 1
1 + 8까지
12
'''
import sys

n, m = map(int, sys.stdin.readline().split())
board = []

def select():
    answer = float('inf')

    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            # answer = min(answer, check(i, j))
            # print(i, j, i + 8, j + 8)
            answer = min(answer, check_v2(i, j))


    print(answer)

'''
'''
white = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]

black = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]

def check_v2(y, x):
    white_cnt = 0
    black_cnt = 0

    for i in range(8):
        for j in range(8):
            if white[i][j] != board[i + y][j + x]:
                white_cnt += 1
            if black[i][j] != board[i + y][j + x]:
                black_cnt += 1

    return min(white_cnt, black_cnt)

def check(y, x):
    toggle = board[y][x]

    # if toggle == 'W':
    #     toggle = 'B'
    # else:
    #     toggle = 'W'

    cnt = 0

    for i in range(y, y + 8):

        if toggle == 'W':
            toggle = 'B'
        else:
            toggle = 'W'

        for j in range(x, x + 8):
            if board[i][j] != toggle:
                cnt += 1

            if toggle == 'W':
                toggle = 'B'
            else:
                toggle = 'W'


    return cnt

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))


select()