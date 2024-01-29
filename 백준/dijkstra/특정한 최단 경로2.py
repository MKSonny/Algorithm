import heapq

n, m = map(int, input().split())

node = [[] for _ in range(n + 1)]

for _ in range(m):
    starting, ending, weight = map(int, input().split())
    node[starting].append((ending, weight))
    node[ending].append((starting, weight))

must_start, must_end = map(int, input().split())


def dijkstra(fix_start):
    dist = [float('inf')] * (n + 1)
    dist[fix_start] = 0
    h = []

    heapq.heappush(h, (fix_start, 0))
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

    return dist

ori = dijkstra(1)
must_start_dist = dijkstra(must_start)
must_end_dist = dijkstra(must_end)

v1 = ori[must_start] + must_start_dist

if asw == float('inf'):
    print(-1)
else:
    print(asw)