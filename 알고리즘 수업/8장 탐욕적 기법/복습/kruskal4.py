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
        self.set_size = self.set_size - 1


def kruskal(vertex, weight):
    n = len(vertex)
    E = []
    sets = disJointSet(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if weight[i][j] != None:
                E.append((i, j, weight[i][j]))

    E.sort(key = lambda o:o[2])
    ecount = n

    for i in range(len(E)):
        v = E[i]
        e1 = sets.find(v[0])
        e2 = sets.find(v[1])
        if e1 != e2:
            sets.union(e1, e2)
            sets.set_size -= 1
            ecount += 1
            if ecount == n - 1:
                break

    print_path(sets.parent)

    print(sets.parent)

def print_path(parent):
    for i in range(len(parent)):
        id = i
        print("Path for vertex %s:" % vertex[id], end=' ')
        while parent[id] >= 0:
            print("%s <- " % vertex[id], end='')
            id = parent[id]
        print("%s" % vertex[id])

# final [5, 6, 3, 4, 5, -1, 3]
kruskal(vertex, weight)