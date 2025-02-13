import heapq
import sys

n = int(sys.stdin.readline())

h = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(h) == 0: print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, a)
