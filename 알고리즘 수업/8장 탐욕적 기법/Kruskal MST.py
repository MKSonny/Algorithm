class disjointSets:
    def __init__(self, n):
        # parent = [-1, -1, -1, -1, -1, -1, -1]
        self.parent = [-1] * n
        # 여기서 set_size의 의미는 부분 그래프의 갯수다.
        self.set_size = n

    # 부모 노드를 찾는 함수
    def find(self, id):
        while self.parent[id] >= 0:
            id = self.parent[id]
        return id

    # 이전 강의에서 봤던 합집합 찾기에서
    # 대소 비교를 했는데 여기에서는 모조건 a < b라서 필요없다.
    def union(self, s1, s2):
        self.parent[s1] = s2
        self.set_size = self.set_size - 1


def MSTKruskal(V, adj):
    n = len(V)
    dsets = disjointSets(n)
    print('dsets', dsets.parent)
    print('set_size', dsets.set_size)
    E = []

    for i in range(n - 1):
        for j in range(i + 1, n):
            if adj[i][j] != None:
                # 여기서 i와 j가 의미하는 것은?
                # (0, 1, 29), 0과 1노드가 29의 비용으로 연결되어 있다.
                E.append((i, j, adj[i][j]))

    print(E)

    # 비용을 기준으로 정렬해라
    E.sort(key=lambda e:e[2])

    print(E)

    ecount = 0 # 간선의 갯수

    for i in range(len(E)):
        e = E[i]

        # 연결된 두 노드의 부모 노드를 찾는다.
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        # 만약 부모가 서로 다르다면
        # 연결되어있지 않다는 의미, 연결해준다.
        if uset != vset:
            # union을 하면서 자동으로 사이클 확인? if 문 안에 들어왔다는 것은
            # 부모가 다르다는 의미 부모가 같은, 같은 그래프에 있는 노드는
            # 여기를 못들어온다.
            dsets.union(uset, vset)
            print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
            ecount += 1
            # 간서의 개수가 노드의 개수 - 1이면 반복을 종료한다.
            if ecount == n - 1:
                break

    print('set_size', dsets.set_size)


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
print("MST by Kruskal's Algorithm")
MSTKruskal(vertex, weight)