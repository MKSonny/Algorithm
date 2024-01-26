import heapq

n, m = map(int, input().split())

node = [[] for _ in range(n + 1)]
dist = [float('inf')] * (n + 1)
dist[1] = 0

for _ in range(m):
    starting, ending, weight = map(int, input().split())
    node[starting].append((ending, weight))
    node[ending].append((starting, weight))

h = []

heapq.heappush(h, (1, 0))
while h:
    start2, weight = heapq.heappop(h)
    # visited[start2] = True

    if dist[start2] < weight:
        continue
    else:
        for key in node[start2]:
            # if not visited[key[0]]:
            if weight + key[1] < dist[key[0]]:
                dist[key[0]] = weight + key[1]
                heapq.heappush(h, (key[0], dist[key[0]]))

print(dist[n])