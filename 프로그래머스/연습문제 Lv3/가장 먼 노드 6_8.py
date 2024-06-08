import heapq

def solution(n, edge):
    answer = 0

    node = [[] for _ in range(n + 1)]

    for i in edge:
        node[i[0]].append((i[1], 1))
        node[i[1]].append((i[0], 1))

    h = []
    INF = float('inf')
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[1] = 0
    heapq.heappush(h, (0, 1))

    while h:
        weight, node_number = heapq.heappop(h)
        visited[node_number] = True

        if weight > dist[node_number]:
            continue

        for key in node[node_number]:
            if not visited[key[0]]:
                if key[1] + weight < dist[key[0]]:
                    dist[key[0]] = key[1] + weight
                    heapq.heappush(h, (dist[key[0]], key[0]))

    maxx = max(dist[1:])

    for i in range(1, n + 1):
        if maxx == dist[i]:
            answer += 1

    return answer