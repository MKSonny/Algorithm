states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]

g = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

def isSafe(g, v, c, color):
    for i in range(len(g)):
        if g[v][i] == 1 and color[i] == c:
            return False

    return True

def DFS_graph_coloring(g, v, k, color):
    if v == len(g):
        return True

    for c in range(1, k + 1):
        if isSafe(g, v, c, color):
            color[v] = c
            # print('a')
            if DFS_graph_coloring(g, v + 1, k, color):
                return True
            color[v] = 0

    return False

def graphColoring(g, k):
    color = [0] * len(g)
    ret = DFS_graph_coloring(g, 0, k, color)
    print(ret)
    if ret:
        for i in range(len(g)):
            print("%s ="%states[i], color_name[color[i]])
    else:
        print('fase')

graphColoring(g, 3)