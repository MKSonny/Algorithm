import heapq
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra(l, dist, n, cnt):
    h = []
    heapq.heappush(h, (l[0][0], 0, 0))
    dist[0][0] = 0

    while h:
        cost, y, x = heapq.heappop(h)

        if y == n - 1 and x == n - 1:
            print(f"Problem {cnt}: {dist[n - 1][n - 1]}")
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                new_cost = cost + l[ny][nx]

                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(h, (new_cost, ny, nx))

INF = float('inf')
cnt = 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    l = []

    for _ in range(n):
        l.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dist = [[INF for _ in range(n)] for _ in range(n)]

    dijkstra(l, dist, n, cnt)
    cnt += 1