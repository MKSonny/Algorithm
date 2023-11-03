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
    # visited
    found = [False] * vsize
    found[start] = True

    # print('dist', dist)

    for i in range(vsize):
        print("Step%2d: " % (i + 1), dist)
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
            if found[w] == False:
                # dist[u] -> 현재 내가 찾은 가장 짧은 비용
                # adj[u][w] -> 내가 찾은 가장 짧은 간선을 제외한 다른 간선들로 갔을 때의 경우들
                # dist[w] ->
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

print('path', path)

# for end in range(len(vertex)):
#     if end != start:
#         print("[최단경로: %s -> %s] %s" % (vertex[start], vertex[end], vertex[end]), end='')
#         while path[end] != start:
#             print(" <- %s" % vertex[path[end]], end='')
#             end = path[end]
#
#     print(" <- %s" % vertex[path[end]])