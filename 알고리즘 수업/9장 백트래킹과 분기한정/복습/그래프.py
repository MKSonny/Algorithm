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

def isSafe(weight, level, colors, c):
    for i in range(len(weight)):
        if weight[level][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(weight, level, k, colors):
    if level == len(weight):
        return True

    for c in range(1, k + 1):
        if isSafe(weight, level, colors, c):
            colors[level] = c
            if graph_coloring(weight, level + 1, k, colors):
                return True
            colors[level] = 0

    return False

colors = [0] * len(g)
graph_coloring(g, 0, 3, colors)
for i in range(len(g)):
    print("%s : %s" %(states[i], color_name[colors[i]]))