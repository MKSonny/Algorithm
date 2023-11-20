g = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]
states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]

def isSafe(g, v, c, color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False
    return True

def DFS_graph_coloring(graph, k, v, color):
    if v == len(graph):
        return True

    for c in range(1, k + 1):
        color[v] = c
        if DFS_graph_coloring(graph, k, v + 1, color):
            return True
        color[v] = 0

    return False

def graphColoring(graph, k, states):
    color = [0] * len(graph)
    ret = DFS_graph_coloring(graph, k, 0, color)
    if ret:
        for i in range(len(graph)):
            print("%3s = " %states[i], color_name[color[i]])
    else:
        print('false')

graphColoring(g, 3, states)