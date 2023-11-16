import copy

def shortest_path_floyd(vertex, W):
    vsize = len(vertex)
    # D0: 아무런 정즘을 거치지 않 경로

    D = copy.deepcopy(W)

    for i in range(vsize):
        for j in range(vsize):
            for k in range(vsize):
                # D[i][k] + D[k][j]: i에서 j로 갈 때 k를 거쳐서 가는 경우
                # D[i][j]: i에서 j로 바로 가는 경우
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
        printD(D)

def printD(D):
    vsize = len(D)
    print("=======================================")
    for i in range(vsize):
        for j in range(vsize):
            if D[i][j] == INF:
                print("  INF  ", end='')
            else:
                print("%4d  "%D[i][j], end='')
        print("")

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
print("Shortest Path By Floyd's Alogorithm")
shortest_path_floyd(vertex, weight)