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

peoples, parties = map(int, input().split())
who_knows_truth = list(map(int, input().split()))
print(who_knows_truth[1:])
party = []

for i in range(parties):
    party.append(list(map(int, input().split())))

parent = [-1] * (peoples + 1)

for p in party:
    # p[0] = 2
    #
    # print('a')
    for i in range(1, p[0]):
        # print('a')
        for j in range(i + 1, p[0] + 1):
            parent[p[i]] = p[j]

cnt = 0

for p in party:
    for e in p:
        if parent[e] in who_knows_truth[1:]:
            cnt += 1
            # print('a')

print(len(party) - cnt)