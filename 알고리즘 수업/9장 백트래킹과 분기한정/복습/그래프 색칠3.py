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

def isSafe(adj, colors, c):
    for i in range(len(adj)):
        if adj[i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(graph, colors, level, k):
    if level == len(graph):
        return True

    for c in range(1, k + 1):
        if isSafe(graph[level], colors, c):
            colors[level] = c
            if graph_coloring(graph, colors, level + 1, k):
                return True
            colors[level] = 0

    return False

colors = [0] * len(g)
print(graph_coloring(g, colors, 0, 3))
for i in range(len(g)):
    print("%s: %s" %(states[i], color_name[colors[i]]))

'''
색상 3개:
 NT =  빨강
 WA =  초록
  Q =  초록
 SA =  파랑
NSW =  빨강
  V =  초록
'''