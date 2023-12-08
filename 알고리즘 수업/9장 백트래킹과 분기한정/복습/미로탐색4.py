maze = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 2],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def isSafe(x, y, maze, mark):
    W, H = len(maze[0]), len(maze)

    if x >= 0 and x < W and y >= 0 and y < H:
        if mark[y][x] != 1 and maze[y][x] != 0:
            return True

    return False

def dfsMaze(maze, x, y, sol, mark):
    if not isSafe(x, y, maze, mark):
        return False

    sol[y][x] = 1
    mark[y][x] = 1

    if maze[y][x] == 2:
        return True

    if dfsMaze(maze, x - 1, y, sol, mark):
        return True
    if dfsMaze(maze, x + 1, y, sol, mark):
        return True
    if dfsMaze(maze, x, y - 1, sol, mark):
        return True
    if dfsMaze(maze, x, y + 1, sol, mark):
        return True

    sol[y][x] = 0

    return False

W, H = len(maze[0]), len(maze)
sol = [[0 for _ in range(W)] for _ in range(H)]
mark = [[0 for _ in range(W)] for _ in range(H)]

dfsMaze(maze, 3, 0, sol, mark)
for i in sol:
    print(i)