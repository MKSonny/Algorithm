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

def isSafe(adj, level, colors, c):
    for i in range(len(adj)):
        if adj[level][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(g, colors, level, k):
    if level == len(g):
        return True

    for c in range(1, k + 1):
        if isSafe(g, level, colors, c):
            colors[level] = c
            if graph_coloring(g, colors, level + 1, k):
                return True
            colors[level] = 0

    return False

def color_graph(g, states, color_name, k):
    colors = [0] * len(g)
    tot = graph_coloring(g, colors, 0, k)
    if tot:
        for i in range(len(g)):
            print("%3s : %s" % (states[i], color_name[colors[i]]))
    else:
        print("색칠할 수 없음")

color_graph(g, states, color_name, 4)
'''
색상 3개:
 NT =  빨강
 WA =  초록
  Q =  초록
 SA =  파랑
NSW =  빨강
  V =  초록
'''