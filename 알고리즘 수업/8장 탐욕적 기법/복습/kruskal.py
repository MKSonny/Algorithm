class joint:
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

def kruskal_mst(vertex, weight):
    n = len(vertex)
    dsets = joint(n)
    graph = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if weight[i][j] != None:
                graph.append((i, j, weight[i][j]))

    graph.sort(key = lambda o : o[2])

    for i in range(n):
        e = graph[i]

        u1 = dsets.find(e[0])
        u2 = dsets.find(e[1])

        ecount = 0

        if u1 != u2:
            dsets.union(u1, u2)
            ecount += 1
            if ecount == n - 1:
                break

    return dsets



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

# final [5, 6, 3, 4, 5, -1, 3]
print(kruskal_mst(vertex, weight).parent)