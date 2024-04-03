import heapq
import sys

n, m, k, start = map(int, sys.stdin.readline().split())

h = []
INF = int(1e9)

dist = [INF] * (n + 1)
visited = [False] * (n + 1)
node = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append((b, 1))

# print(node)
# dist[start] = 0
heapq.heappush(h, (0, start))

while h:
    weight, node_number = heapq.heappop(h)
    visited[node_number] = True
    #0, dist[1] = 0
    if weight > dist[node_number]:
        continue
    # 연결된 간선 정보
    for key in node[node_number]:
        # (2, 1), (3, 1)
        if not visited[key[0]]:
            if weight + key[1] < dist[key[0]]:
                dist[key[0]] = weight + key[1]
                heapq.heappush(h, (dist[key[0]], key[0]))

# print(dist)
cnt = 0
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)