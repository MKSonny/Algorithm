INF = 9999
vertex = ['A', 'B', 'C', 'D', 'E']
weight = [
   # A  B  C  D  E
    [None, 7, 4, None, 2],
    [7, None, None, 3, 4],
    [4, None, None, 6, 3],
    [None, 3, 6, None, 5],
    [2, 4, 3, 5, None]
]

def getMinVertex(dist, selected):
    min = INF
    min_v = -1

    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i

    return min_v

def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    path = [-1] * vsize
    dist[0] = 0
    selected = [False] * vsize

    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=':')
        print(dist)
        for v in range(vsize) : # 내부 루프
            if (adj[u][v] != None): # (u,v) 간선이 있으면 dist[v] 갱신
                if selected[v]==False and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
                    path[v] = u
    print(path)
    total = 0
    for i in range(1,vsize) :
        print("(%d,%d)=%d"%(i, path[i], adj[i][path[i]]))
        total += adj[i][path[i]]
    print("total weight =", total)

MSTPrim(vertex, weight)