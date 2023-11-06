def is_safe(maze, x, y, mark):
    W, H = len(maze[0]), len(maze)
    if x >= 0 and x < W and y >= 0 and y < H:
        if maze[y][x] != 0 and mark[y][x] == 0:
            return True
        return False

def find_way(maze, x, y):
    W, H = len(maze[0]), len(maze)
    sol = [[0 for _ in range(W)] for _ in range(H)]
    mark = [[0 for _ in range(W)] for _ in range(H)]
    if dfs(maze, x, y, sol, mark) == False:
        print("길을 찾을 수 없습니다.")
    else:
        for i in sol:
            print(i)

def dfs(maze, x, y, sol, mark):
    if not is_safe(maze, x, y, mark):
        return False

    sol[y][x] = 1
    mark[y][x] = 1

    if maze[y][x] == 2:
        return True

    if dfs(maze, x + 1, y, sol, mark):
        return True
    if dfs(maze, x - 1, y, sol, mark):
        return True
    if dfs(maze, x, y + 1, sol, mark):
        return True
    if dfs(maze, x, y - 1, sol, mark):
        return True

    sol[y][x] = 0
    return False

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

find_way(maze, 3, 0)