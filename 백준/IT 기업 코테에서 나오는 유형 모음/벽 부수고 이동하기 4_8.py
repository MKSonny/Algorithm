import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(y, x, z):
    q = deque()
    q.append((y, x, z))

    while q:
        a, b, c = q.popleft()

        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                # 다음 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
                if graph[ny][nx] == 1 and c == 0:
                    visited[ny][nx][1] = visited[a][b][0] + 1
                    q.append((ny, nx, 1))
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                elif graph[ny][nx] == 0 and visited[ny][nx][c] == 0:
                    visited[ny][nx][c] = visited[a][b][c] + 1
                    q.append((ny, nx, c))

    return -1

print(bfs(0, 0, 0))