from collections import deque
import copy


def solution(maps):
    answer = 0

    # L까지 가는 곳의 최소 거리를 구한 후
    # 다시 L부터 BFS 탐색 시작

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    N = len(maps)
    M = len(maps[0])

    def bfs(start, end):
        visited = [[False for _ in range(M)] for _ in range(N)]
        q = deque([])
        flag = True

        for i in range(N):
            for j in range(M):
                if maps[i][j] == start:
                    q.append((i, j, 0))
                    visited[i][j] = True
                    flag = False
                    break
            if flag == False: break

        while q:
            y, x, cost = q.popleft()
            # visited[y][x] = True
            if maps[y][x] == end:
                return cost
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx] and maps[ny][nx] != 'X':
                        q.append((ny, nx, cost + 1))
                        visited[ny][nx] = True

        return -1

    temp1 = bfs('S', 'L')
    temp2 = bfs('L', 'E')

    if temp1 != -1 and temp2 != -1:
        return temp1 + temp2
    else:
        return -1