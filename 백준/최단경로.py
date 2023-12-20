import heapq

n, m = map(int, input().split())
start = int(input())

h = []
INF = 9999
dist = [INF] * (n + 1)
dist[1] = 0

for _ in range(m):
    v1, v2, w = map(int, input().split())
    heapq.heappush(h, (w, v2))

for _ in range(m):
    print(heapq.heappop(h))