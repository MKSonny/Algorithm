# 중요) prim과 kruskal 결과 다름

INF = 9999
vertex = ['A', 'B', 'C', 'D', 'E']
weight = [
   # A  B  C  D  E
    [None, 7, 4, None, 2],
    [7, None, None, 3, 4],
    [4, None, None, 6, 3],
    [None, 3, 6, None, 5],
    # [2, 4, 3, 5, None]
    [2, 4, 3, 5, None]
]

class disJointSet:
    def __init__(self, n):
        self.parent = [-1] * n
        self.set_size = n

    def find(self, id):
        while self.parent[id] >= 0:
            id = self.parent[id]
        return id

    def union(self, s1, s2):
        self.parent[s1] = s2
        self.set_size -= 1

def kruskal_mst(vertex, weight):
    n = len(vertex)
    s = disJointSet(n)
    E = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            if weight[i][j] != None:
                E.append((i, j, weight[i][j]))

    E.sort(key= lambda e:e[2])
    ecount = 0

    for i in range(len(E)):
        e = E[i]
        e1 = s.find(e[0])
        e2 = s.find(e[1])
        if e1 != e2:
            ecount += 1
            s.union(e1, e2)
            if ecount == n - 1:
                break

    print(s.parent)

def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i
    return min_v

def prim(vertex, weight):
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0
    selected = [False] * n

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if weight[u][j] != None:
                if not selected[j] and weight[u][j] < dist[j]:
                    dist[j] = weight[u][j]
        # print("dist: %s =" % vertex[u], dist)

    print(dist)

prim(vertex, weight)
kruskal_mst(vertex, weight)