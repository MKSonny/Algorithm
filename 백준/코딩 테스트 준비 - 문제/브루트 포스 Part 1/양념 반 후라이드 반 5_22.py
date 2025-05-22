import sys


a, b, c, x, y = map(int, sys.stdin.readline().split())
min_total = a * x + b * y
min_x_y = min(x, y)

for i in range(2, 100000 * 2 + 1, 2):
    first = a * (x - i // 2)
    second = b * (y - i // 2)

    if y - i // 2 < 0:
        second = 0
    if x - i // 2 < 0:
        first = 0

    total = first + second + c * i
    min_total = min(total, min_total)

print(min_total)