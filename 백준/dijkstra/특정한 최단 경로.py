import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

node = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    node[start].append((end, weight))

INF = float("inf")
dist = [INF] * (n + 1)

must_start, must_end = map(int, input().split())

h = []
heapq.heappush(h, (0, must_start))

while h:
    weight, starting = heapq.heappop(h)
    for k in node[starting]:
        if k[1] + weight < dist[k[0]]:
            dist[k[0]] = k[1] + weight
            heapq.heappush(h, (dist[k[0]], k[0]))

print(dist)