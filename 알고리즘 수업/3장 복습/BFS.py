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
        for b in nbr:
            q.put(b)
            visited.add(b)

bfs(mygraph, 'A')