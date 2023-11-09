g = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

# graph[1][i] = [1, 0, 0, 1, 0, 0]
# c = [1, 0, 0, 0, 0, 0]
states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]

def isSafe(graph, v, color, c):
    for i in range(len(color)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def dfs_color_graph(graph, k, v, color):
    if v == len(graph[0]):
        return True

    for c in range(1, k + 1):
        if isSafe(graph, v, color, c):
            color[v] = c
            # print(color)
            if dfs_color_graph(graph, k, v + 1, color):
                return True
            color[v] = 0

    return False
color = [0] * len(g[0])
print(dfs_color_graph(g, 3, 0, color))
print(dfs_color_graph(g, 2, 0, color))
