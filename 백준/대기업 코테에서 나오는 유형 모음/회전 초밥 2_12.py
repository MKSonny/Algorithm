import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())

plate = []

for _ in range(N):
    plate.append(int(sys.stdin.readline()))

maxx = 0
cnt = 0
eat = deque()

for i in range(k - 1):
    eat.append(plate[i])

for j in range(N):
    eat.append(plate[(j + k - 1) % N])
    cnt = 0
    if c not in eat:
        cnt = 1
    maxx = max(len(set(eat)) + cnt, maxx)
    eat.popleft()

print(maxx)