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

def isSafe(adj, level, c, colors):
    for i in range(len(adj)):
        if adj[level][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(g, level, color_name, colors, k):
    if level == len(g):
        return True

    for c in range(1, k + 1):
        if isSafe(g, level, c, colors):
            colors[level] = c
            if graph_coloring(g, level + 1, color_name, colors, k):
                return True
            colors[level] = 0
    return False

def do_graph_coloring(states, color_name, k):
    colors = [0] * len(g)
    to = graph_coloring(g, 0, color_name, colors, k)
    if to:
        for i in range(len(g)):
            print("%s ->" % states[i], color_name[colors[i]])
    else:
        print("불가")

do_graph_coloring(states, color_name, 3)