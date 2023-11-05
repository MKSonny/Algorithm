import queue

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

def bfs(graph, start):
    visited = { start }
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        v = q.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for n in nbr:
            q.put(n)
            visited.add(n)


bfs(mygraph, 'A')