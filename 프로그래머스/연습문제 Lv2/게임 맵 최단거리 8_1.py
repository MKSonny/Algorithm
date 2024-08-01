from collections import deque


def solution(maps):
    answer = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    n = len(maps)
    m = len(maps[0])

    s = deque([(0, 0)])
    maps[0][0] = 1
    cnt = 1
    while s:
        y, x = s.popleft()
        cnt += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    s.append((ny, nx))

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]