n = int(input())
m = int(input())
a = []

for _ in range(m):
    a.append(list(map(int, input().split())))

# print(a)

class disJointSet:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
        self.set_size = n

    def find(self, id):
        while self.parent[id] >= 0:
            id = self.parent[id]
        return id

    def union(self, s1, s2):
        self.parent[s1] = s2
        self.set_size -= 1

def Kruskal(n, a):
    dsets = disJointSet(n)
    a.sort(key=lambda o : o[2])
    ecount = 0
    min_total = 0

    for i in range(len(a)):
        e = a[i]

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
            min_total += e[2]
            # print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
            ecount += 1
            # 간서의 개수가 노드의 개수 - 1이면 반복을 종료한다.
            if ecount == n - 1:
                break

    return min_total

print(Kruskal(n, a))