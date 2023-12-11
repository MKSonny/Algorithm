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

class disJointSets:
    def __init__(self, n):
        self.parent = [-1] * n
        self.set_size = n

    def find(self, id):
        while self.parent[id] >= 0:
            id = self.parent[id]
        return id

    def union(self, s1, s2):
        self.parent[s1] = s2
        self.set_size = self.set_size - 1


def kruskal(vertex, weight):
    n = len(vertex)
    dsets = disJointSets(n)
    E = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            if weight[i][j] != None:
                E.append((i, j, weight[i][j]))

    E.sort(key = lambda o:o[2])

    for i in range(len(E)):
        v = E[i]
        e1 = dsets.find(v[0])
        e2 = dsets.find(v[1])

        if e1 != e2:
            dsets.union(e1, e2)
            if dsets.set_size == 1:
                break

    print(dsets.parent)

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
    selected = [False] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if weight[u][j] != None:
                if weight[u][j] < dist[j] and not selected[j]:
                    dist[j] = weight[u][j]

    return dist

print(prim(vertex, weight))
# final [5, 6, 3, 4, 5, -1, 3]
kruskal(vertex, weight)