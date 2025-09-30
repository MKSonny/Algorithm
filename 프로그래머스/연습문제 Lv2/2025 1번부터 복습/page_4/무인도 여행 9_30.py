from collections import deque


def solution(maps):
    answer = []

    n, m = len(maps), len(maps[0])

    for i in range(n):
        maps[i] = list(maps[i])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(y, x):
        q = deque([(y, x)])
        total = int(maps[y][x])
        maps[y][x] = 'X'

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx] != 'X':
                        q.append((ny, nx))
                        total += int(maps[ny][nx])
                        maps[ny][nx] = 'X'

        return total

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                answer.append(bfs(i, j))

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer