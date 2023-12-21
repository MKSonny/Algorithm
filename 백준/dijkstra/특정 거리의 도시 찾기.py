import heapq
import sys

input = sys.stdin.readline

n, m, k, start = map(int, input().split())

node = [[] for _ in range(n + 1)]

for _ in range(m):
    starting, ending = map(int, input().split())
    node[starting].append((ending, 1))

INF = float("inf")
dist = [INF] * (n + 1)
visited = [False] * (n + 1)

h = []
heapq.heappush(h, (0, start))
while h:
    weight, start2 = heapq.heappop(h)
    visited[start2] = True
    if weight > dist[start2]:
        continue
    for key in node[start2]:
        if not visited[key[0]]:
            if key[1] + weight < dist[key[0]]:
                dist[key[0]] = key[1] + weight
                heapq.heappush(h, (dist[key[0]], key[0]))

cnt = 0

# print(dist)

for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)
