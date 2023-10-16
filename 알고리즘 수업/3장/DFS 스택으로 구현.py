mygraph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

def dfs_stack(graph, start):
    visited = set()
    v_list = []
    v_list.append(start)

    while v_list:
        v = v_list.pop()

        if v not in visited:
            visited.add(v)
            print(v, end=' ')

        nbr = graph[v] - visited
        for n in nbr:
            v_list.append(n)

# A B D C E H G F
dfs_stack(mygraph, 'A')