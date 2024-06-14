from collections import deque


def solution(maps):
    answer = []

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def bfs(y, x, visited):
        q = deque([(y, x)])
        visited[y][x] = True
        t = 0
        while q:
            y, x = q.popleft()
            t += int(maps[y][x])
            # print(maps[y][x])
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx].isdigit() and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
        return t

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j].isdigit() and not visited[i][j]:
                answer.append(bfs(i, j, visited))

    if len(answer) == 0:
        return [-1]
    answer.sort()

    return answer