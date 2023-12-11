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

# https://www.youtube.com/watch?v=pVfj6mxhdMw
# vertex = ['A', 'B', 'C', 'D', 'E']
# weight = [
#     [0, 6, INF, 1, INF],
#     [6, 0, 5, 2, 2],
#     [INF, 5, 0, INF, 5],
#     [1, 2, INF, 0, 1],
#     [INF, 2, 5, 1, 0],
# ]
'''
            dist[i]: 이것은 현재 소스 정점에서 정점 i까지의 현재 최단 거리를 나타냅니다.
            dist[u]: 이것은 현재 소스 정점에서 현재 중간 정점 u까지의 최단 거리입니다.
            weight[u][i]: 이것은 정점 u에서 정점 i로 향하는 간선의 가중치입니다.
            따라서 dist[i] = min(dist[i], dist[u] + weight[u][i])는 다음과 같이 말합니다: 
            정점 i로의 현재 최단 거리(dist[i])를 현재 중간 정점 u를 통한 거리와 정점 u에서 i로의 간선 가중치의 합의 최소값으로 업데이트하십시오.

            간단하게 말하면 이것은 현재 중간 정점 u를 통해 정점 i까지의 더 짧은 경로가 있는지 확인하고, 있다면 정점 i까지의 현재 알려진 최단 거리를 업데이트하는 Dijkstra 알고리즘의 핵심 단계입니다.
            '''
def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v

    return minv

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    # found == selected
    found = [False] * vsize
    found[start] = True

    for i in range(vsize):
        # print("Step%2d: " % (i + 1), dist)
        u = getMinVertex(dist, found)
        # print('u', u)
        # 가장 싼 비용 찾음
        found[u] = True

        # u: 현재 처리 중인 노드(정점)입니다.
        # u는 이전 단계에서 이미 방문한 노드 중에서 최단 경로를 가진 노드를 나타냅니다.
        # 즉, 현재까지의 최단 경로가 발견된 노드입니다.

        # w: 아직 방문하지 않은 노드 중에서 현재 처리 중인 노드 u와 연결된 노드를 나타냅니다.
        # 즉, w는 u와 직접 연결된 노드 중에서 최단 경로를 찾고자 하는 노드입니다.
        for w in range(vsize):
            # 가장 싼 비용이 아닌 것과 현재 시작 점이 아닌 것 중에서
            # 11.14 방문한 지점이 아니라면
            if found[w] == False:
                # dist[u] -> 현재 내가 찾은 가장 짧은 비용
                # adj[u][w] -> 내가 찾은 가장 짧은 간선을 제외한 다른 간선들로 갔을 때의 경우들

                # dist[w]: w로 직접 갔을 때보다 adj[u][w]를 통해 경유해서 갔을 때가 더 빠른 경우
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
                    print(dist)
    print('dist:', dist)
    return path

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)):
    if end != start:
        print(vertex[start], "->", vertex[end], end='')

    vlist = [end]
    while path[end] != start:
        vlist.insert(0, path[end])
        end = path[end]
    vlist.insert(0, start)

    dist = 0
    for i in range(1, len(vlist)):
        dist += weight[vlist[i - 1]][vlist[i]]

    print("\t", dist, "\t", vlist)
