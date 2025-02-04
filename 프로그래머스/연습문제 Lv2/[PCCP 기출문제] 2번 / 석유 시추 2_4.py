from collections import deque


def solution(land):
    answer = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    n = len(land)
    m = len(land[0])

    di = {}

    def bfs(y, x, visited, idx):
        q = deque([(y, x)])
        visited[y][x] = idx
        cnt = 0

        while q:
            y, x = q.popleft()
            cnt += 1

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        q.append((ny, nx))
                        visited[ny][nx] = idx

        di[idx] = cnt

        return cnt

    visited = [[False for _ in range(m)] for _ in range(n)]

    idx = 2

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j, visited, idx)
                idx += 1

    maxx = -1

    for j in range(m):
        t = []
        for i in range(n):
            if visited[i][j] >= 2 and visited[i][j] not in t:
                t.append(visited[i][j])
        c = 0
        for k in t:
            c += di[k]
        maxx = max(c, maxx)

    return maxx