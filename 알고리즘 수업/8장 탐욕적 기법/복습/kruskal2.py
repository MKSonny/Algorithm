class disJointset:
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

def kruskal(vertex, adj):
    n = len(vertex)
    s = disJointset(n)
    E = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            if adj[i][j] != None:
                E.append((i, j, adj[i][j]))

    E.sort(key=lambda e:e[2])
    e_count = 0

    for i in range(len(E)):
        e = E[i]
        e1 = s.find(e[0])
        e2 = s.find(e[1])
        if e1 != e2:
            e_count += 1
            s.union(e1, e2)
            if e_count == n - 1:
                break

    print(s.parent)

# final [5, 6, 3, 4, 5, -1, 3]
kruskal(vertex, weight)