class disJointSets:
    def __init__(self, n):
        self.parent = [-1] * n
        self.set_size = n

    def find(self, id):
        while self.parent[id] >= 0:
            id = self.parent[id]
        return id

    def union(self, s1, s2):
        # 여기서 s1은 자식 s2가 부모다.
        self.parent[s1] = s2
        self.set_size = self.set_size - 1



def MSTKurskal(V, adj):
    n = len(V)
    dsets = disJointSets(n)
    E = []

    '''
    이와 같이 반복하는 이유는 양방양 그래프에서는 대각선을 기준으로
    같은 숫자가 반복되서 나타난다. 따라서 대각선을 기준으로 계단 형식으로
    반복하여 중복을 피한다.
    
    이 중첩된 반복문은 그래프의 모든 간선을 한 번씩 검사하기 위해 사용됩니다. 
    이중 반복문을 사용하여 모든 가능한 (i, j) 쌍을 생성하면 모든 간선을 검사할 수 있습니다. 
    여기서 i와 j는 그래프의 노드를 나타냅니다. 
    이렇게 생성된 (i, j) 쌍은 각각 그래프의 노드들을 연결하는 간선을 나타냅니다.
    '''
    for i in range(n - 1):
        for j in range(i + 1, n):
            if adj[i][j] is not None:
                E.append((i, j, adj[i][j]))

    E.sort(key=lambda e:e[2])

    ecount = 0
    score = 0

    for i in range(len(E)):
        # 비용이 가장 작은 간선을 확인한다.
        e = E[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        if uset != vset:
            dsets.union(uset, vset)
            score += e[2]
            ecount += 1
            if ecount == n - 1:
                break

    print(score)
    # final [5, 6, 3, 4, 5, -1, 3]
    print(dsets.parent)

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

MSTKurskal(vertex, weight)