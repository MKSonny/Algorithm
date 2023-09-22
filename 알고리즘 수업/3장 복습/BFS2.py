mygraph = [
    #A, B, C, D, E, F, G, H
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def dfs(graph, start, visited):
    if start not in visited:
        print(vertex[start], end=' ')
        visited.append(start)
        v = graph[start]
        for i in range(8):
            if v[i] == 1:
                dfs(graph, i, visited)

dfs(mygraph, 0, [])