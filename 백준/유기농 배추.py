t = int(input())

cnt = 0

def dfs(a, row, col, visited):
    global cnt
    global max_row, max_col
    if row > max_row or row < 0 or col > max_col or col < 0:
        return
    if a[row][col] == 1 and visited[row][col] == 0:
        cnt += 1
        visited[row][col] = 1
        # left
        dfs(a, row, col - 1, visited)
        # right
        dfs(a, row, col + 1, visited)
        # up
        dfs(a, row - 1, col, visited)
        # down
        dfs(a, row + 1, col, visited)

for k in range(t):
    data = list(map(int, input().split()))
    field = [[0 for _ in range(data[0])] for _ in range(data[1])]
    visited = [[0 for _ in range(data[0])] for _ in range(data[1])]
    max_row = data[1]
    max_col = data[0]
    for i in range(data[2]):
        location = list(map(int, input().split()))
        x = location[1]
        y = location[0]
        field[x][y] = 1
    for i in range(data[1]):
        for j in range(data[0]):
            dfs(field, i, j, visited)

for row in field:
    print(row)