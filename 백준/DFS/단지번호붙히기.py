n = int(input())

maze = []

for i in range(n):
    maze.append(list(map(int, input())))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

cnt = 0

def dfs(maze, y, x):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if maze[y][x] == 1:
        global cnt
        cnt += 1
        maze[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(maze, ny, nx)
        return True

    return False

num = []
result = 0

for i in range(n):
    for j in range(n):
        if dfs(maze, i, j):
            num.append(cnt)
            result += 1
            cnt = 0

print(result)
num.sort()
for li in num:
    print(li)