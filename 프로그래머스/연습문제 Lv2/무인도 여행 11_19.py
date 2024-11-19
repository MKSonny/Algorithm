from collections import deque


def solution(maps):
    answer = []

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def bfs(y, x):
        q = deque([(y, x)])
        total = 0
        visited[y][x] = True

        while q:
            y, x = q.popleft()
            total += int(maps[y][x])

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
        return total

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))

    answer.sort()
    if len(answer) == 0:
        return [-1]

    return answer