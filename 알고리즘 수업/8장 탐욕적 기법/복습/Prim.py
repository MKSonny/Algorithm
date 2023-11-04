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

def find_min_route(dict, selected):
    min = INF
    min_v = -1
    for v in range(len(dict)):
        if dict[v] < min and selected[v] == False:
            min = dict[v]
            min_v = v
    return min_v

'''
Prim MST vs Dijkstra’s algorithm
1. Dijkstra’s algorithm finds the shortest path, but Prim’s algorithm finds the MST.
Dijkstra는 최단경로를, Prim은 최소 신장 트리를 찾아준다.
어느 한 쪽이 다른 한 쪽을 보장해 줄 수 없다.

2. Dijkstra’s algorithm can work on both directed and undirected graphs, but Prim’s algorithm only works on undirected graphs.
Prim은 무방향 그래프에서만 동작한다. Dijkstra는 상관없다.

3. Prim’s algorithm can handle negative edge weights, but Dijkstra’s algorithm may fail to accurately compute distances if at least one negative edge weight exists.
Prim은 음의 가중치를 가진 간선에서도 잘 동작한다. Dijkstra는 이상한 결과가 나올 수도 있다.
'''

# 언제 weight가 필요한가?
# prim의 mst의 역할을 이해하지 못하고 있다.
def prim_mst(vertex, weight):
    vsize = len(vertex)
    selected = [False] * vsize
    dict = [INF] * vsize
    dict[0] = 0 # 시작점을 설정?

    for i in range(vsize):
        u = find_min_route(dict, selected)
        selected[u] = True
        # 이후 dict에서 할 수 있는 것은 없다.
        # 정확히 dict의 역할은 무엇인가?
        for v in range(vsize):
            # 아래는 무엇을 의미하는가?
            # u = 현재 선택한 노드
            # v = 갈 수 있는 간선들
            if weight[u][v] != None:
                if weight[u][v] < dict[v] and selected[v] == False:
                    # 최솟값으로 업데이트 -> 할 필요가 없나? 위에서 해주는데..
                    # 그럼 갈 수 있는 길을 모두 적는다.
                    # 그 이후에는?
                    dict[v] = weight[u][v]

        print(vertex[u], end=':')
        print(dict)

print("MST by Prim's Algoritm")
prim_mst(vertex, weight)

'''
MST by Prim's Algoritm
A:[0, 29, 9999, 9999, 9999, 10, 9999]
F:[0, 29, 9999, 9999, 27, 10, 9999]
E:[0, 29, 9999, 22, 27, 10, 25]
D:[0, 29, 12, 22, 27, 10, 18]
C:[0, 16, 12, 22, 27, 10, 18]
B:[0, 16, 12, 22, 27, 10, 15]
G:[0, 16, 12, 22, 27, 10, 15]
'''