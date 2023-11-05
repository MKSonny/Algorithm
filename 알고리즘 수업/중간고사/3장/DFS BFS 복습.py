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

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

def select_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[least] > A[j]:
                least = j
        A[least], A[i] = A[i], A[least]

print("before sort", data)
select_sort(data)
print("after sort", data)

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        # 다음 방문할 노드가 갈 수 있는 곳에서
        # 이미 방문한 노드를 제외한다.
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

def bfs(graph, start):
    visited = { start }
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            q.put(u)

dfs(mygraph, 'A', set())
print()
bfs(mygraph, 'A')