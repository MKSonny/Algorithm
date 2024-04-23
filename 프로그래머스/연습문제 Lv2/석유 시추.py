import copy
from collections import deque

def solution(land):
    answer = 0

    H = len(land)
    W = len(land[0])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    number = dict()
    num = 2

    def bfs(y, x, l, H, W, num):

        q = deque()

        q.append((y, x))
        l[y][x] = num

        cnt = 1

        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < H and 0 <= nx < W:
                    if l[ny][nx] == 1:
                        cnt += 1
                        l[ny][nx] = num
                        q.append((ny, nx))

        number[num] = cnt


    for i in range(H):
        for j in range(W):
            if land[i][j] == 1:
                bfs(i, j, land, H, W, num)
                num += 1

    k = []

    for j in range(W):
        type = set()
        total = 0
        for i in range(H):
            if land[i][j] != 0:
                type.add(land[i][j])
        for item in type:
            total += number[item]

        k.append(total)

    answer = max(k)

    return answer