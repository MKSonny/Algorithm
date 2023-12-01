

INF = 9999

board = [
    [5, 5, 4],
    [3, 9, 1],
    [3, 2, 7]
]

W, H = len(board[0]), len(board)

dist = [[INF for _ in range(W)] for _ in range(H)]

dist[0][0] = 5

for i in dist:
    print(i)

can_go = []

def find_can_go(board, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print('x, y', x, y)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < W and ny >= 0 and ny < H:
            dist[ny][nx] = dist[y][x] + board[ny][nx]
            can_go.append((ny, nx))

    for i in dist:
        print(i)

    return can_go

for i in can_go:
    print(i[0])

selected = []

def getMinVertex(board, can_go, selected):
    min = INF
    min_v = -1
    for i in can_go:
        if board[i[0]][i[1]] < min and i not in selected:
            min = board[i[0]][i[1]]
            min_v = i
    return min_v

for i in dist:
    print(i)

def dijkstra(board):
    a = [(0, 0)]
    selected = []
    while len(a) != 0:
        vertex = a.pop()
        # print(vertex)
        y, x = vertex[0], vertex[1]
        can_go = find_can_go(board, x, y)
        # print('can_go', can_go)
        u = getMinVertex(board, can_go, selected)
        selected.append(u)
        a.append(u)

dijkstra(board)

for i in dist:
    print(i)