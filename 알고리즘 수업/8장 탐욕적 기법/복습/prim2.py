def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and selected[i] == 0:
            min = dist[i]
            min_v = i
    return min_v

def prim(weight, vertex):
    n = len(vertex)
    dist = [INF] * n
    selected = [0] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = 1
        for j in range(n):
            if weight[u][j] != None:
                if weight[u][j] < dist[j] and selected[j] == 0:
                    dist[j] = weight[u][j]
        print(dist)


INF = 9999
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [None, 29, None, None, None, 10, None],
    [29, None, 16, None, None, None, 15],
    [None, 16, None, 12, None, None, None],
    [None, None, 12, None, 22, None, 18],
    [None, None, None, 22, None, 27, 25],
    [10, None, None, None, 27, None, None],
    [None, 15, None, 18, 25, None, None]
]

prim(weight, vertex)