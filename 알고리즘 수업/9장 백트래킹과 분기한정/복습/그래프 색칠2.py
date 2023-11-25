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

def isSafe(g, v, colors, c):
    for i in range(len(g)):
        if g[v][i] == 1 and colors[i] == c:
            return False
    return True

def do_coloring(g, k, states, color_name):
    colors = [0] * len(g)
    ret = coloring(g, 0, k, colors)
    if ret:
        for i in range(len(states)):
            print("%3s ="% states[i], color_name[colors[i]])
    else:
        print("else")

def coloring(g, v, k, colors):
    if v == len(g):
        return True

    for c in range(1, k + 1):
        if isSafe(g, v, colors, c):
            colors[v] = c
            if coloring(g, v + 1, k, colors):
                return True
            colors[v] = 0

    return False

do_coloring(g, 4, states, color_name)