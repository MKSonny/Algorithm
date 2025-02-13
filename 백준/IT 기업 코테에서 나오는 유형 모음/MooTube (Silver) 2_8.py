import sys
sys.setrecursionlimit(100000)

n, k = map(int, sys.stdin.readline().split())

lo = []

an = []

no = [[] for _ in range(n + 1)]
aq = []

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    no[a].append((b, c))
    no[b].append((a, c))

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    aq.append((a, b))
# 1 -> 2 -> 3 : 2
# 1 -> 2: 3

def dfs(q, i, visited, sc):
    # no[i] # 여러개 2가 나오면 no[2]를 통해서 갈 수 있는 모든 경로 구해야 함
    for a, b in no[i]:
        # b에 있음 sc
        if i != a and not visited[a]:
            q.append((a, min(sc, b)))
            visited[a] = True
            dfs(q, a, visited, b)
    return q
# print()
#
# for i in no:
#     print(i)
# print()

an = [[]]

for i in range(1, n + 1):
    q = []
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    sc = float('inf')
    an.append(dfs(q, i, visited, sc))

# for i in an: print(i)

for a, b in aq:
    cnt = 0

    for t, sc in an[b]:
        # print(sc, a)
        if sc >= a:
            cnt += 1

    print(cnt)