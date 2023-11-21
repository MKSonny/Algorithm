INF = 9999
vertex = ['A', 'B', 'C', 'D', 'E']
weight = [
   # A  B  C  D  E
    [None, 7, 4, None, 2],
    [7, None, None, 3, 4],
    [4, None, None, 6, 3],
    [None, 3, 6, None, 5],
    [2, 4, 3, 5, None]
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
    dist[0] = 0
    selected = [False] * n

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if weight[u][j] != None:
                if not selected[j] and weight[u][j] < dist[j]:
                    dist[j] = weight[u][j]

        print(vertex[u], end=':')
        print(dist)

prim(vertex, weight)