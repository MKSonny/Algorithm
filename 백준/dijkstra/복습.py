import heapq

n, m, k, start = map(int, input().split())

node = [[] for _ in range(n + 1)]

for _ in range(m):
    starting, ending = map(int, input().split())
    node[starting].append((ending, 1))

dist = [float('inf')] * (n + 1)
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
