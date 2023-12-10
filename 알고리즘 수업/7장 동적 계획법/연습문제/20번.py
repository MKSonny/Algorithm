import copy

INF = 9999

W = [
    [0, 7, 9, INF, INF, 14],
    [7, 0, 10, 15, INF, 21],
    [9, 10, 0, 11, INF, 23],
    [INF, 15, 11, 0, 6, INF],
    [INF, INF, INF, 6, 0, 9],
    [14, 21, 23, INF, 9, 0]
]

def tcf(W):
    vsize = len(W)
    D = copy.deepcopy(W)

    for i in range(vsize):
        for j in range(vsize):
            if D[i][j] == INF:
                D[i][j] = 0
            else:
                D[i][j] = 1

    for i in D:
        print(i)


    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if D[i][j] == 0:
                    if D[i][k] and D[k][j]:
                        D[i][j] = 1




tcf(W)