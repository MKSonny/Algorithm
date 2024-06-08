import heapq


class disjointsets:
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


def mst_kruskal(t, costs, answer):
    n = len(costs)
    dsets = disjointsets(t)
    costs.sort(key=lambda o: o[2])
    ecount = 0

    for i in range(n):
        e = costs[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        if uset != vset:
            dsets.union(uset, vset)
            ecount += 1
            answer += e[2]

            if ecount == t - 1:
                break
    return answer


def solution(n, costs):
    return mst_kruskal(n, costs, 0)