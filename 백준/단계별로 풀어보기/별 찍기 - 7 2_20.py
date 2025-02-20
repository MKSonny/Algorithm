import sys

n = int(sys.stdin.readline())


# 4, 1, 4
# 3, 3, 3
# 2, 5, 2
# 1, 7, 1
# 0, 9, 0

while n >= 0:
    for i in range(n - 1, -1, -1):
        print(' ', end='')
    for j in range():
        print('*', end='')
    for i in range(n - 1, -1, -1):
        print(' ', end='')
    print()

    n -= 1