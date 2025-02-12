import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())

plate = []

for _ in range(N):
    plate.append(int(sys.stdin.readline()))

print(plate)
plate += plate
print(plate)
idx = 0
print()

def check(start):
    idx = start
    q = []
    maxx = k
    flag = True
    while idx < 2 * N:
        if plate[idx] == c and flag:
            maxx += 1
            flag = False

        if len(q) == maxx:
            print(q, set(q))
            return len(set(q))

        q.append(plate[idx])

        idx += 1

maxx = 1
for i in range(N):
   maxx = max(maxx, check(i))
print(maxx)


