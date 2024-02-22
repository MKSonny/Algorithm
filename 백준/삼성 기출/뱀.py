n = int(input())
k = int(input())

l = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    l[r - 1][c - 1] = 'a'

# for i in l:
#     print(i)

k = int(input())
dir = []

for _ in range(k):
    c, d = input().split()
    dir.append((c, d))

# print(dir)

y = 0
x = 0
cnt = 0

# first = dir.pop(0)
# print('first', first)
idx = 0
toggle = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

snake = [(0, 0)]
# l[0][0] = 's'

while 0 <= y < n and 0 <= x < n:
    if l[y][x] == 's':
        break
    if cnt == int(dir[dir_idx][0]):
        # dir_cnt += 1
        # print('cnt', cnt)
        # print('direction', dir[dir_idx][1])
        # print('dir_idx', dir_idx)
        if dir[dir_idx][1] == 'D':
            idx += 1
        else:
            idx -= 1
        # print('cnt', cnt)
        if dir_idx < k - 1:
            dir_idx += 1
        # first = dir.pop(0)

    dy, dx = toggle[idx % 4]

    # x += dx
    # y += dy

    # print(y, x)

    # l[y][x] = cnt

    if l[y][x] == 'a':
        l[y][x] = 's'
        snake.append((y, x))
    else:
        l[y][x] = 's'
        snake.append((y, x))
        ty, tx = snake.pop(0)
        l[ty][tx] = 'n'

    # print(snake)
    # for i in l:
    #     print(i)

    # print(y, x)

    cnt += 1
    x += dx
    y += dy

# print()
#
# for i in l:
#     print(i)
#
print(cnt)

# l = int(input())
#
# for _ in range(l):
#     x, c =