INF = 9999
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, INF, INF, 3, 10, INF],
    [7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [3, 2, INF, 11, 0, 13, 5],
    [10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

def getMinVertex(dist, selected):
    min = INF
    min_v = -1

    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i

    return min_v

def dijkstra(vertex, weight):
    n = len(vertex)
    dist = [INF] * n
    selected = [False] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(u)
        for j in range(n):
            if dist[u] + weight[u][j] < dist[j]:
                dist[j] = dist[u] + weight[u][j]

    print(dist)


dijkstra(vertex, weight)