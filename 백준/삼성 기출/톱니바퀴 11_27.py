import sys
from collections import deque

gears = deque()

for _ in range(4):
    gears.append(deque(list(map(int, sys.stdin.readline().rstrip()))))

n = int(sys.stdin.readline())

how = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    how.append((a - 1, b))

def right(idx, d):
    if idx > 3:
        return
    if gears[idx - 1][2] != gears[idx][6]:
        right(idx + 1, -d)
        gears[idx].rotate(d)

def left(idx, d):
    if idx < 0:
        return
    if gears[idx][2] != gears[idx + 1][6]:
        left(idx - 1, -d)
        gears[idx].rotate(d)

for a, b in how:
    left(a - 1, -b)
    right(a + 1, -b)
    gears[a].rotate(b)

score = 0
for i in range(4):
    if gears[i][0]:
        score += 2 ** i

print(score)