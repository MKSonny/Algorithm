import sys
from collections import deque
import copy

board = []
# x가 하나더 많아야 한다.

def check_right_cross(t, y, x, prev):
    # if t[y][x] == prev:
    # left, right | up, down
    dy = [-1, 1]
    dx = [1, -1]
    q = deque([(y, x)])

    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[y][x] = True

    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1

        if cnt == 3:
            # print("check_right_cross")

            return True

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 3 and 0 <= nx < 3:
                if t[ny][nx] == prev and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

def check_left_cross(t, y, x, prev):
    # print("check_left_cross")
    # if t[y][x] == prev:
    # left, right | up, down
    dy = [-1, 1]
    dx = [-1, 1]
    q = deque([(y, x)])

    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[y][x] = True

    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1

        if cnt == 3: return True

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 3 and 0 <= nx < 3:
                if t[ny][nx] == prev and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True

def check_up_down(t, y, x, prev):
    # if t[y][x] == prev:
    # left, right | up, down
    # print("check_up_down")
    dy = [-1, 1]
    q = deque([(y, x)])


    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[y][x] = True

    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1

        if cnt == 3: return True

        for i in range(2):
            ny = y + dy[i]
            if 0 <= ny < 3 and t[ny][x] == prev and not visited[ny][x]:
                q.append((ny, x))
                visited[ny][x] = True

    return False

def check_left_right(t, y, x, prev):
    # if t[y][x] == prev:
    # left, right | up, down
    # print("check_left_right")
    dx = [-1, 1]
    q = deque([(y, x)])


    visited = [[False for _ in range(3)] for _ in range(3)]
    visited[y][x] = True

    cnt = 0

    while q:
        y, x = q.popleft()
        cnt += 1
        if cnt == 3: return True
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < 3 and t[y][nx] == prev and not visited[y][nx]:
                q.append((y, nx))
                visited[y][nx] = True

    return False


total_answer = []

while True:
    t = sys.stdin.readline().rstrip()
    if t == 'end':
        break

    di = {'X': deque() , 'O': deque()}

    t_board = [['.' for _ in range(3)] for _ in range(3)]
    answer = [[] for _ in range(3)]
    # board.append(list(t))

    for idx, i in enumerate(list(t)):
        if i in di.keys():
            di[i].append((idx // 3, idx % 3))

    # if di['X'] <= di['O']:
    #     board.append('invalid')
    # else:
    #     if di['X'] - di['O'] > 1:
    #         board.append('invalid')
    #         continue
    #     board.append('valid')

    options = []

    # print(di)
    for idx, i in enumerate(list(t)):
        if 0 <= idx < 3:
            answer[0].append(i)
        elif 3 <= idx < 6:
            answer[1].append(i)
        else:
            answer[2].append(i)

    # print('answer')
    # for i in answer:
    #     print(i)
    # print()

    flagA = False
    flagB = False

    while True:
        if len(di['X']):
            y, x = di['X'].popleft()
            t_board[y][x] = 'X'

            if check_left_right(t_board, y, x, 'X') or check_up_down(t_board, y, x, 'X') or check_left_cross(t_board, y, x, 'X') or check_right_cross(t_board, y, x, 'X'):
                # print('X win')
                # for i in t_board:
                #     print(i)
                # print()
                temp = copy.deepcopy(t_board)
                options.append(temp)
                flagA = True
        else:
            # flagA = True
            break

        if len(di['O']):
            y, x = di['O'].popleft()
            t_board[y][x] = 'O'
            if check_left_right(t_board, y, x, 'O') or check_up_down(t_board, y, x, 'O') or check_left_cross(t_board, y, x, 'O') or check_right_cross(t_board, y, x, 'O'):
                # print('O win')
                # for i in t_board:
                #     print(i)
                # print()
                temp = copy.deepcopy(t_board)
                options.append(temp)
                flagB = True
        else:
            # flagB = True
            break

    if flagA == False and flagB == False:

        # print('****************************')
        # for i in t_board:
        #     print(i)
        # print()
        # print('****************************')


        f = False
        for i in range(3):
            for j in range(3):
                if answer[i][j] == '.':
                    # total_answer.append("invalid")
                    f = True
                    break
            if f: break

        if f:
            total_answer.append("invalid")
            continue

        if answer == t_board:
            total_answer.append("valid")
            continue


    if answer in options:
        total_answer.append("valid")
        # print("====================================")
        # for i in answer:
        #     print(i)
        # print("options")
        # for i in options:
        #     for j in i:
        #         print(j)
        #     print()
        # print("====================================")
        continue

    else:
        total_answer.append("invalid")
        continue
    # print("options")
    # for i in options:
    #     for j in i:
    #         print(j)
    #     print()

    # for i in t_board:
    #     print(i)
    # print()

# print(len(total_answer))
for i in total_answer:
    print(i)