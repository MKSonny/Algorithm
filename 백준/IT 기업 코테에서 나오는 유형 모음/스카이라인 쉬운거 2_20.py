import sys


n = int(sys.stdin.readline())
skyline_y_x = []
max_x, max_y = -1, -1

for _ in range(n):
    y, x = map(int, sys.stdin.readline().split())
    skyline_y_x.append((y, x))

    max_x = max(max_x, x)
    max_y = max(max_y, y)


print(max_y, max_x)
skyline = [['.' for _ in range(max_y + 1)] for _ in range(max_x + 1)]

for i in skyline:
    print(i)

for y, x in skyline_y_x:
    if x == 0: continue
    skyline[x - 1][y - 1] = 'X'

print()
for i in skyline:
    print(i)