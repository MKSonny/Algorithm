import queue

n, m = map(int, input().split())
graph = []
for i in range(n):
    list = map(int, list(input()))
    graph.append(list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
