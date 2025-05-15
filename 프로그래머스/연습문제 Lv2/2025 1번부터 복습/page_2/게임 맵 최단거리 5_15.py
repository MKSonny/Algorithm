from collections import deque


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(y, x):
        q = deque([(y, x)])

        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if maps[ny][nx] == 1:
                        maps[ny][nx] = maps[y][x] + 1
                        q.append((ny, nx))

    bfs(0, 0)

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]

    return answer