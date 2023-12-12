INF = 999
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

def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i
    return min_v


def prim(vertex, weight):
    n = len(vertex)
    dist = [INF] * n
    selected = [False] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if not selected[j] and weight[u][j] != None:
                if weight[u][j] < dist[j]:
                    dist[j] = weight[u][j]
        print(i + 1, dist)

    return dist

print(prim(vertex, weight))