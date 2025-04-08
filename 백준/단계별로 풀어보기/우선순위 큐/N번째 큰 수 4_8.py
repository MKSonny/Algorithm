import sys
import heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    if len(h) == 0:
        for i in l:
            heapq.heappush(h, i)
    else:
        for i in l:
            if h[0] < i:
                heapq.heappush(h, i)
                heapq.heappop(h)

print(h[0])