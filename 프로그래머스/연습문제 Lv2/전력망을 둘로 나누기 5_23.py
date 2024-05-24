import copy
from collections import deque

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

l = [[] for _ in range(n + 1)]
for a, b in wires:
    l[a].append(b)
    l[b].append(a)

cnt_l = []

for a, b in wires:
    print('a, b', a, b)
    temp = copy.deepcopy(l)
    temp[a].remove(b)
    temp[b].remove(a)

    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        q = deque([i])
        cnt = 1
        visited[i] = True

        while q:
            v = q.popleft()
            print(v, end=' ')
            for i in temp[v]:
                if not visited[i]:
                    cnt += 1
                    q.append(i)
                    visited[i] = True

        print()

        cnt_l.append(cnt)
    print(cnt_l)