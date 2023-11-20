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

def is_safe(maze, mark, x, y):
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y >= 0 and y < H:
        if maze[y][x] != 0 and mark[y][x] == 0:
            return True
    return False

def dfs(maze, sol, mark, x, y):
    if not is_safe(maze, mark, x, y):
        return False

    sol[y][x] = 1
    mark[y][x] = 1

    if maze[y][x] == 2:
        return True

    if dfs(maze, sol, mark, x - 1, y):
        return True
    if dfs(maze, sol, mark, x + 1, y):
        return True
    if dfs(maze, sol, mark, x, y - 1):
        return True
    if dfs(maze, sol, mark, x, y + 1):
        return True

    sol[y][x] = 0
    return False


def find_way(maze, x, y):
    W, H = len(maze[0]), len(maze)
    sol = [[0 for _ in range(W)] for _ in range(H)]
    mark = [[0 for _ in range(W)] for _ in range(H)]
    if dfs(maze, sol, mark, x, y) == False:
        print("길 없음")
    else:
        for i in sol:
            print(i)


find_way(maze, 3, 0)
