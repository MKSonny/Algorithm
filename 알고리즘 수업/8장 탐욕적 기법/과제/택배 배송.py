n, m = map(int, input().split())

INF = 99999999

# weight = [[INF for _ in range(n)] for _ in range(n)]
weight = [[] for _ in range(n)]

for _ in range(m):
    start, end, t_weight = map(int, input().split())
    weight[start - 1].append((end - 1, t_weight))
    weight[end - 1].append((start - 1, t_weight))


def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i
    return min_v
def dijkstra(weight):
    n = len(weight)
    dist = [INF] * n
    selected = [False] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        edges = weight[u]
        for edge in edges:
            if not selected[edge[0]]:
                if dist[u] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[u] + edge[1]

    print(dist[n - 1])

dijkstra(weight)