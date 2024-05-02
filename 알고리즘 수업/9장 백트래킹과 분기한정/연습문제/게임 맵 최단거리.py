from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# cnt = 1

def solution(maps):
    answer = 0

    #     for i in maps:
    #         print(i)
    #     print()

    W = len(maps[0])
    H = len(maps)

    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True

    # if maps[H - 1 - 1][W - 1] == 0 and maps[H - 1][W - 1 - 1] == 0

    def print_map(maps):
        for i in maps:
            print(i)
        print()

    def bfs(maps, y, x):
        # global cnt
        q = deque()
        q.append((y, x))
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < H and 0 <= nx < W:
                    if not visited[ny][nx] and maps[ny][nx] >= 1:
                        maps[ny][nx] = maps[y][x] + 1
                        visited[ny][nx] = True
                        # print_map(maps)
                        q.append((ny, nx))

    bfs(maps, 0, 0)

    if maps[H - 1][W - 1] == 1:
        return -1
    else:
        return maps[H - 1][W - 1]

    return answer