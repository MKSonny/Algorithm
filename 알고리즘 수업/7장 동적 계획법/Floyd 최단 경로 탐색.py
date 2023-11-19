import copy

def shortest_path_floyd(vertex, W):
    vsize = len(vertex)
    # D0: 아무런 정즘을 거치지 않는 경로

    D = copy.deepcopy(W)

    # 이렇게 반복하면 A가 경유지가 되는 것 같다.
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                # D[i][k] + D[k][j]: i에서 j로 갈 때 k를 거쳐서 가는 경우
                # D[i][j]: i에서 j로 바로 가는 경우
                # print(D[i][k], D[k][j], D[i][j])
                # 11.19
                # 첫 반복은 A를 경유지로 설정하고, i는 고정 j는 증가하면..
                # A -> A + A -> (A ~ G) < A -> (A ~ G)
                # i = 1
                # B -> A + A -> (A ~ G) < B -> (A ~ G)
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
# D[i][k] + D[k][j] < D[i][j]:
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