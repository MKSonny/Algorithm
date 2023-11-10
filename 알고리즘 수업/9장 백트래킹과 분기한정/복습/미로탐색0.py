def isSafe(x, y, maze, mark):
    if x >= 0 and x < len(maze[0]) and y >=0 and y < len(maze):
        if maze[y][x] != 0 and mark[y][x] == 0:
            return True
    return False

def dfs(maze, x, y, sol, mark):

    if not isSafe(x, y, maze, mark):
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

sol = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
mark = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]

# for i in sol:
#     print(i)

print(dfs(maze, 3, 0, sol, mark))
for i in sol:
    print(i)