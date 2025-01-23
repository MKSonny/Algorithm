import sys

# n = int(sys.stdin.readline().rstrip())
# l = []
#
# for _ in range(n):
#     l.append(list(map(int, sys.stdin.readline().split())))

n = 5

test = [[0 for _ in range(n)] for _ in range(n)]
test[n // 2][n // 2] = 1

# [2][4] -> [0][2]
# [2][3] -> [1][2]
# [2][2] -> [2][2]
# [2][1] -> [3][2]
# [2][0] -> [4][2]

# [n][k] -> [k - 4][n]

for i in test:
    print(i)

print()


def rotate(test):
    rotated = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[n - j - 1][i] = test[i][j]
    return rotated


cnt = 0
temp = 1
y, x = 2, 2


def print_test(test):
    for i in test:
        print(i)
    print()


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

mul = [2, 10, 7, 1, 5, 10, 7, 1, 2, 0]
wy = [
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0],
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1]
      ]
wx = [
      [0, -1, 0, 1, -2, -1, 0, 1, 0, -1],
      [-2, -1, -1, -1, 0, 1, 1, 1, 2, 0],
      [0, 1, 0, -1, 2, 1, 0, -1, 0, 1],
      [2, 1, 1, 1, 0, -1, -1, -1, -2, 0]
]

while True:
    



def do(cnt, temp, y, x):
    while True:
        dx, dy = dir[cnt % 4]

        for _ in range(temp):
            x += dx
            y += dy
            test[y][x] = 1

        print_test()

        if cnt % 2 == 1:
            temp += 1

        cnt += 1

        # test = rotate(test)


# do()
calc(test, 2, 0)



