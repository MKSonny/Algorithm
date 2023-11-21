'''
최소비용 신장트리는 연결 그래프에만 적용할 수 있다.
그렇다면 Prim의 알고리즘을 적용하기 전에 그래프가 연결그래프인지를 먼저 확인해야 할까?
아니면 Prim의 알고리즘에서 바로 처리가 가능할까?

getlMinVertex()에서 정점의 인덱스와 그 정점까지의 거리를 반환하도록 하고,
거리가 무한대이면 연결된 그래프가 아니다.
'''


def getMinVertex(distances, mstSet):
    minDist = float('inf')
    minVertex = -1

    for v in range(len(distances)):
        if distances[v] < minDist and not mstSet[v]:
            minDist = distances[v]
            minVertex = v

    return minVertex, minDist


def prim(graph):
    numVertices = len(graph)
    parent = [-1] * numVertices
    distances = [float('inf')] * numVertices
    mstSet = [False] * numVertices

    # 임의의 시작 정점을 선택
    startVertex = 0
    distances[startVertex] = 0

    while False in mstSet:
        # 현재까지의 거리 중 최소 거리를 가진 정점 선택
        currentVertex, currentDistance = getMinVertex(distances, mstSet)

        # 해당 정점을 트리에 추가
        mstSet[currentVertex] = True

        # 연결된 정점들을 확인하여 거리 업데이트
        for vertex in range(numVertices):
            if graph[currentVertex][vertex] > 0 and not mstSet[vertex] and graph[currentVertex][vertex] < distances[
                vertex]:
                distances[vertex] = graph[currentVertex][vertex]
                parent[vertex] = currentVertex

    # 최소 신장 트리 출력
    for i in range(1, numVertices):
        print(f"Edge: {parent[i]} - {i}, Weight: {graph[i][parent[i]]}")


# 그래프 예시
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 0, 0, 0, 0]
]

prim(graph)
