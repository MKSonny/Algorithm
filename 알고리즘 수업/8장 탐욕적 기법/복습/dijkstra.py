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
# vertex = ['A', 'B', 'C', 'D', 'E']
# weight = [
#     [0, 6, INF, 1, INF],
#     [6, 0, 5, 2, 2],
#     [INF, 5, 0, INF, 5],
#     [1, 2, INF, 0, 1],
#     [INF, 2, 5, 1, 0],
# ]

# prim: [0, 2, 4, 2, 3, 6, 4]
# mst: 간선들의 비용 최소화
# dijkstra: [0, 5, 9, 11, 3, 10, 8]

def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and selected[i] == False:
            min = dist[i]
            min_v = i

    return min_v

def dijkstra(vertex, weight):
    n = len(vertex)
    dist = [INF] * n
    selected = [False] * n
    dist[0] = 0

    for j in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print('go to', vertex[u])
        for i in range(n):
            '''
            dist[i]: 이것은 현재 소스 정점에서 정점 i까지의 현재 최단 거리를 나타냅니다.
            dist[u]: 이것은 현재 소스 정점에서 현재 중간 정점 u까지의 최단 거리입니다.
            weight[u][i]: 이것은 정점 u에서 정점 i로 향하는 간선의 가중치입니다.
            따라서 dist[i] = min(dist[i], dist[u] + weight[u][i])는 다음과 같이 말합니다: 
            정점 i로의 현재 최단 거리(dist[i])를 현재 중간 정점 u를 통한 거리와 정점 u에서 i로의 간선 가중치의 합의 최소값으로 업데이트하십시오.

            간단하게 말하면 이것은 현재 중간 정점 u를 통해 정점 i까지의 더 짧은 경로가 있는지 확인하고, 있다면 정점 i까지의 현재 알려진 최단 거리를 업데이트하는 Dijkstra 알고리즘의 핵심 단계입니다.
            '''
            if weight[u][i] != INF and selected[i] == False:
                dist[i] = min(dist[i], dist[u] + weight[u][i])

        print('dist', dist)


dijkstra(vertex, weight)