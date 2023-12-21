import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

node = [[] for _ in range(n + 1)]

for i in range(m):
    start, end, weight = map(int, input().split())
    node[start].append((end, weight))

for_start, for_end = map(int, input().split())

# print(node)

h = []
heapq.heappush(h, (0, for_start))
INF = float("inf")
dist = [INF] * (n + 1)

while h:
    weight, starting = heapq.heappop(h)
    if weight > dist[starting]:
        continue
    for k in node[starting]:
        if weight + k[1] < dist[k[0]]:
            dist[k[0]] = weight + k[1]
            heapq.heappush(h, (dist[k[0]], k[0]))

print(dist[for_end])