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

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

# dfs(mygraph, 'A', set())

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

# bfs(mygraph, 'A')

def binary_search(a, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return binary_search(a, left, mid - 1, key)
        else:
            return binary_search(a, mid + 1, right, key)

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[least], a[i] = a[i], a[least]

data = [3, 9, 1, 4, 2]
print(data)
selection_sort(data)
print(data)

idx = binary_search(data, 0, len(data) - 1, 4)
print(idx)