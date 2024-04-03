import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

node = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, weight = map(int, sys.stdin.readline().split())
    node[a].append((b, weight))

h = []

heapq.heappush(h, (0, start))

visited = [False] * (v + 1)
INF = float("inf")
dist = [INF] * (v + 1)
dist[start] = 0

while h:
    weight, node_number = heapq.heappop(h)
    visited[node_number] = True
    if weight > dist[node_number]:
        continue
    for key in node[node_number]:
        if not visited[key[0]]:
            if weight + key[1] < dist[key[0]]:
                dist[key[0]] = weight + key[1]
                heapq.heappush(h, (dist[key[0]], key[0]))

for i in range(1, v + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])