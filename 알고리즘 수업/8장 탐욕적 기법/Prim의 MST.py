def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v

    return minv

# 1. 시작 노드에서 경로들을 조사하고 최소 경로를 찾고 해당 vertex를 반환한다.
# 2. 해당 vertex를 visited에 추가한다.
# 3. 그리고 해당 노드에서 다시 최소 경로를 찾고 해당 vertex를 반환한다.

def MSTPrim(vertex, weight):
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[0] = 0
    selected = [False] * vsize

    for i in range(vsize):
        # 처음에는 전부 INF니까 u = 0
        u = getMinVertex(dist, selected)
        selected[u] = True


        for v in range(vsize):
            # u는 선택된 vertex
            # weight[u][v]는 해당 vertex가 갈 수 있는 길들의 목록
            if weight[u][v] != None: # 해당 길로 갈 수 있다면
                # if selected[v] == False: 갔던 길이 아니라면
                # weight[u][v] < dist[v]
                # dist가 나타내는 것?
                if selected[v] == False and weight[u][v] < dist[v]:
                    dist[v] = weight[u][v]

        print(vertex[u], end=':')
        print(dist)

# 조건1: 방문 했던 곳을 표시할 것
# 조건2: 최소 경로를 다니며 갱신할 것
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

print("MST by Prim's Algoritm")
MSTPrim(vertex, weight)