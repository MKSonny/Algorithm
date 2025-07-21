from collections import deque


def solution(maps):
    answer = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    def bfs(y, x, option, visited):
        q = deque([(y, x)])

        while q:
            y, x = q.popleft()

            if maps[y][x] == option:
                return y, x, visited[y][x]

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx))

        return -1, -1, -1

    def find_s():
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 'S':
                    return i, j

    fy, fx = find_s()
    # print(fy, fx)
    ly, lx, c = bfs(fy, fx, 'L', visited)

    if ly == -1 and lx == -1:
        return -1

    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[ly][lx] = c

    y, x, answer = bfs(ly, lx, 'E', visited)

    return answer