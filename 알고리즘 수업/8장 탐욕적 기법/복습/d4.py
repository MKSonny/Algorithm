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

def dijkstra(vertex, weight, start):
    n = len(vertex)
    dist = list(weight[start])
    selected = [False] * n
    selected[0] = True
    path = [start] * n

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if not selected[j]:
                if dist[u] + weight[u][j] < dist[j]:
                    dist[j] = dist[u] + weight[u][j]
                    path[j] = u

    return path

start = 0
path = dijkstra(vertex, weight, start)
for end in range(len(vertex)):
    if end != start:
        print("[최단 경로 %s -> %s]: %s" %(vertex[start], vertex[end], vertex[end]), end = "")
        while path[end] != start:
            print(" <- %s" % vertex[path[end]], end="")
            end = path[end]
        print(" <- %s" % vertex[path[end]])

'''
[최단경로: A -> B] B <- E <- A
[최단경로: A -> C] C <- B <- E <- A
[최단경로: A -> D] D <- C <- B <- E <- A
[최단경로: A -> E] E <- A
[최단경로: A -> F] F <- A
[최단경로: A -> G] G <- E <- A
'''