import heapq
import copy


def solution(n, s, a, b, fares):
    answer = 0

    h = []
    heapq.heappush(h, (0, s))
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    visited = [False] * (n + 1)

    node = [[] for _ in range(n + 1)]

    for f in fares:
        node[f[0]].append((f[2], f[1]))
        node[f[1]].append((f[2], f[0]))

    while h:
        weight, node_number = heapq.heappop(h)
        visited[node_number] = True

        if weight > dist[node_number]:
            continue

        for key in node[node_number]:
            if not visited[key[1]]:
                if weight + key[0] < dist[key[1]]:
                    dist[key[1]] = weight + key[0]
                    heapq.heappush(h, (dist[key[1]], key[1]))

    # print(dist)
    ori_dist = copy.deepcopy(dist)

    # print()
    answer = float('inf')

    for i in range(1, n + 1):
        h = []
        dist = [INF] * (n + 1)
        dist[i] = 0
        visited = [False] * (n + 1)
        h = []
        heapq.heappush(h, (0, i))

        while h:
            weight, node_number = heapq.heappop(h)
            visited[node_number] = True

            if weight > dist[node_number]:
                continue

            for key in node[node_number]:
                if not visited[key[1]]:
                    if weight + key[0] < dist[key[1]]:
                        dist[key[1]] = weight + key[0]
                        heapq.heappush(h, (dist[key[1]], key[1]))

        # print("%s까지 합승" % i, dist)
        # print(dist[a], dist[b])
        answer = min(answer, dist[a] + dist[b] + ori_dist[i])

    return answer