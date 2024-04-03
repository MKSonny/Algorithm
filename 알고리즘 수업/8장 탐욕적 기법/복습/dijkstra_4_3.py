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

def getMinVertex(dist, visited):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min:
            min = dist[i]
            min_v = i
    return min_v

def dijkstra(vertex, weight, start):
    vsize = len(vertex)
    dist = weight[start]
    visited = [False] * vsize
    visited[start] = True
    for i in range(vsize):
        u = getMinVertex(dist, visited)
        visited[u] = True
        for j in range(vsize):
            if not visited[j]:
                if dist[u] + weight[u][j] < dist[j]:
                    dist[j] = dist[u] + weight[u][j]

    print(dist)

dijkstra(vertex, weight, 0)