vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print("Visiting:", vertex[start])

    # [0, 1, 1, 0, 0, 0, 0, 0]
    for neighbor, is_connected in enumerate(graph[start]):
        if is_connected == 1 and neighbor not in visited:
            dfs(graph, neighbor, visited)

start_vertex = 0  # 시작 정점을 선택합니다. 예를 들어, 'A'를 시작 정점으로 선택합니다.

dfs(adjMat, start_vertex)