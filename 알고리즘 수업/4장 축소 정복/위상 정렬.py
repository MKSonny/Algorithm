mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

def topological_sort(graph):
    inDeg = {}

    for v in graph:
        inDeg[v] = 0

    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1

    print(inDeg)

    visited = []
    for v in graph:
        if inDeg[v] == 0:
            visited.append(v)

    while visited:
        v = visited.pop()
        print(v, end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                visited.append(u)

topological_sort(mygraph)