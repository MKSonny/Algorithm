import heapq
import sys


n = int(sys.stdin.readline()) # 도시의 개수
m = int(sys.stdin.readline()) # 버스의 개수


node = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, weight = map(int, sys.stdin.readline().split())
    node[a].append((b, weight))

start, end = map(int, sys.stdin.readline().split())

h = []

heapq.heappush(h, (0, start))

INF = float("inf")
dist = [INF] * (n + 1)
visited = [False] * (n + 1)

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

print(dist[end])