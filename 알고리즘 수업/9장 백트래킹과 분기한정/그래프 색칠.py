states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]

def isSafe(g, v, c, color):
    # v = 0, c = 1
    # color = [0, 0, 0, 0, 0, 0]
    for i in range(len(g)):
        # g[v][i] == 1
        # adj를 모두 찾는다.
        # color[i] == c
        # adj 중에서 c와 같은지 찾는다.
        if g[v][i] == 1 and color[i] == c:
            return False
    # adj중에서 color[i] == c가 없을 경우 true를 반환한다.
    return True

def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True

    # c = 1로 시작하는 이유?
    # 노드가 1부터 시작하기 때문?
    for c in range(1, k + 1):
        if isSafe(graph, v, c, color):
            # 1) color[0] = 1
            color[v] = c

            # DFS_graph_coloring(g, k, 2, color)
            if DFS_graph_coloring(g, k, v + 1, color):
                return True
            # 아니면 취소
            color[v] = 0

    return False

def graphColoring(graph, k, states):
    color = [0] * len(graph)
    ret = DFS_graph_coloring(graph, k, 0, color)
    if ret:
        for i in range(len(graph)):
            print("%3s = " % states[i], color_name[color[i]])
    else:
        print("그래프를 색칠할 수 없음")


g = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

print("색상 3개:")
graphColoring(g, 3, states)
print("색상 2개:")
graphColoring(g, 2, states)