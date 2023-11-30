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

def isSafe(maze, x, y, mark):
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y >= 0 and y < H:
        if mark[y][x] == 0 and maze[y][x] != 0:
            return True
    return False

def dfs(maze, x, y, sol, mark):
    if not isSafe(maze, x, y, mark):
        return False

    sol[y][x] = 1
    mark[y][x] = 1

    if maze[y][x] == 2:
        return True

    if dfs(maze, x - 1, y, sol, mark):
        return True
    if dfs(maze, x + 1, y, sol, mark):
        return True
    if dfs(maze, x, y - 1, sol, mark):
        return True
    if dfs(maze, x, y + 1, sol, mark):
        return True

    sol[y][x] = 0
    return False

def find_way(x, y, maze):
    sol = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    mark = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

    if dfs(maze, x, y, sol, mark):
        for i in sol:
            print(i)
    else:
        print("no")

find_way(3, 0, maze)