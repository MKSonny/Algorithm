import heapq


def solution(N, road, K):
    answer = 0

    node = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        node[a].append((c, b))
        node[b].append((c, a))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    visited = [False] * (N + 1)
    h = []
    heapq.heappush(h, (0, 1))
    while h:
        w, n = heapq.heappop(h)
        if w > dist[n]:
            continue
        visited[n] = True
        for k in node[n]:
            if not visited[k[1]]:
                if w + k[0] < dist[k[1]]:
                    dist[k[1]] = w + k[0]
                    heapq.heappush(h, (dist[k[1]], k[1]))
    answer = 1
    for i in range(2, N + 1):
        if dist[i] <= K:
            answer += 1

    return answer