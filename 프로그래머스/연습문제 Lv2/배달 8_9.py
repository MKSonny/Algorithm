import heapq


def solution(N, road, K):
    answer = 1

    h = []
    INF = float('inf')

    node = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    visited = [False] * (N + 1)

    for a, b, c in road:
        node[a].append((b, c))
        node[b].append((a, c))

    heapq.heappush(h, (0, 1))

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

    for i in dist:
        if i <= K:
            answer += 1

    return answer