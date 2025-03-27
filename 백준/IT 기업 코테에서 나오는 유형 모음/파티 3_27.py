import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance = [float('inf') for _ in range(n + 1)]

    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next in graph[cur]:
            cost = dist + next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance


# 2 -> 1, 1 -> 2
maxx = -1
for i in range(1, n + 1):
    if i == x: continue
    maxx = max(dijkstra(i)[x] + dijkstra(x)[i], maxx)

print(maxx)