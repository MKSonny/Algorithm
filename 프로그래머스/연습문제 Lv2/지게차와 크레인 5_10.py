from collections import deque


def solution(storage, requests):
    answer = 0

    l = [['x' for _ in range(len(storage[0]) + 2)]]

    for i in storage:
        temp = ['x']
        temp.extend(list(i))
        temp.append('x')
        l.append(temp)

    l.append(['x' for _ in range(len(storage[0]) + 2)])

    n = len(l)
    m = len(l[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(y, x, r):
        q = deque([(y, x)])
        visited = [[False for _ in range(m)] for _ in range(n)]

        visited[y][x] = True

        while q:
            y, x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx]:
                        if l[ny][nx] == 'x':
                            q.append((ny, nx))
                            visited[ny][nx] = True
                        if l[ny][nx] == r:
                            l[ny][nx] = 'r'

        for i in range(n):
            for j in range(m):
                if l[i][j] == 'r':
                    l[i][j] = 'x'

    for r in requests:
        if len(r) == 1:
            bfs(0, 0, r)
        else:
            for i in range(n):
                for j in range(m):
                    if l[i][j] == r[0]:
                        l[i][j] = 'x'

    for i in l:
        for j in i:
            if j != 'x':
                answer += 1

    return answer