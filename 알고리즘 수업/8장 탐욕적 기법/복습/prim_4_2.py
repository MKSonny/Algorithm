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

def select_node(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i
    return min_v

def mst(vertex, weight):
    v_size = len(vertex)
    dist = [INF] * v_size
    dist[0] = 0
    selected = [False] * v_size
    for i in range(v_size):
        u = select_node(dist, selected)
        selected[u] = True
        for v in range(v_size):
            if weight[u][v] != None:
                if not selected[v] and weight[u][v] < dist[v]:
                    dist[v] = weight[u][v]

    print(dist)

mst(vertex, weight)
