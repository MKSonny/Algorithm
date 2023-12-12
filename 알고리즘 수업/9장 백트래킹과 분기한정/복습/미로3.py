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
        if maze[y][x] != 0 and mark[y][x] != 1:
            return True
    return False

def maze_dfs(maze, x, y, sol, mark):
    if not isSafe(maze, x, y, mark):
        return False

    sol[y][x] = 1
    mark[y][x] = 1

    if maze[y][x] == 2:
        for i in sol:
            print(i)
        return True

    if maze_dfs(maze, x - 1, y, sol, mark):
        return True
    if maze_dfs(maze, x + 1, y, sol, mark):
        return True
    if maze_dfs(maze, x, y - 1, sol, mark):
        return True
    if maze_dfs(maze, x, y + 1, sol, mark):
        return True

    sol[y][x] = 0

    return False

W, H = len(maze[0]), len(maze)
sol = [[0] * W for _ in range(H)]
mark = [[0] * W for _ in range(H)]
maze_dfs(maze, 3, 0, sol, mark)