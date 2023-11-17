import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if 0 < num <= 1000:
        heapq.heappush(heap, num)

sum = 0

while True:
    if len(heap) < 2:
        print(sum)
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    # heap = {10, 20, 30, 40}
    # sum += 30
    # heap = {30, 30, 40}
    # sum += 60
    # heap = {60, 40}
    # sum += 100

    # heap = (10 + 20) + (30 + 30) + (60 + 40)
    sum += a + b
    # heap = {30, 40}
    # heap = {30, 70}
    heapq.heappush(heap, a + b)