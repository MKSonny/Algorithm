def get_min_vertex(dist, selected):
    min_v = -1
    min = INF
    for i in range(len(dist)):
        if dist[i] < min and selected[i] == False:
            min = dist[i]
            min_v = i
    return min_v

def prim_mst(vertex, weight):
    vsize = len(vertex)
    selected = [False] * vsize
    dist = [INF] * vsize
    dist[0] = 0
    for i in range(len(dist)):
        v = get_min_vertex(dist, selected)
        selected[v] = True
        print(dist)
        for j in range(vsize):
            if weight[v][j] != None:
                if dist[j] > weight[v][j] and selected[j] == False:
                    dist[j] = weight[v][j]

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
prim_mst(vertex, weight)