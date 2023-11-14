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
# dijkstra 테스트 weight
# weight = [
#     [None, 7, None, None, 3, 10, None],
#     [7, None, 4, 10, 2, 6, None],
#     [None, 4, None, 2, None, None, None],
#     [None, 10, 2, None, 11, 9, 4],
#     [3, 2, None, 11, None, 13, 5],
#     [10, 6, None, 9, 13, None, None],
#     [None, None, None, 4, 5, None, None]
# ]
def select_node(dist, selected):
    min = INF
    min_v = -1
    for v in range(len(dist)):
        if selected[v] != True and dist[v] < min:
            min = dist[v]
            min_v = v
    return min_v

def mst(vertex, weight):
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[0] = 0
    selected = [False] * vsize
    for i in range(vsize):
        u = select_node(dist, selected)
        selected[u] = True
        for v in range(vsize):
            if weight[u][v] != None:
                if selected[v] == False and weight[u][v] < dist[v]:
                    dist[v] = weight[u][v]
        print(vertex[u], end=': ')
        print(dist)

mst(vertex, weight)