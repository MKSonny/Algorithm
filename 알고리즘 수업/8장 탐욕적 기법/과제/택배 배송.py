n, m = map(int, input().split())

INF = 9999

# weight = [[INF for _ in range(n)] for _ in range(n)]
weight = []

for _ in range(m):
    start, end, t_weight = map(int, input().split())
    weight.append((start, end, t_weight))
    # weight[start - 1][end - 1] = t_weight
    # weight[end - 1][start - 1] = t_weight

for i in weight:
    print(i)

'''

def getMinVertex(dist, selected):
    min = INF
    min_v = -1
    for i in range(len(dist)):
        if dist[i] < min and not selected[i]:
            min = dist[i]
            min_v = i
    return min_v
def dijkstra(weight):
    n = len(weight)
    dist = [INF] * n
    selected = [False] * n
    dist[0] = 0

    for i in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        for j in range(n):
            if not selected[j]:
                if dist[u] + weight[u][j] < dist[j]:
                    dist[j] = dist[u] + weight[u][j]

    print(dist[n - 1])

dijkstra(weight)
'''