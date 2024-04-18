import copy
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move(y, x, n, dist, visited):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if l[ny][nx] + dist[y][x] < dist[ny][nx]:
                dist[ny][nx] = l[ny][nx] + dist[y][x]


    # print('a')
    # for p in dist:
    #     print(p)
    # print()


cnt = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    cnt += 1
    l = []

    visited = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(n):
        l.append(list(map(int, sys.stdin.readline().rstrip().split())))

    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    dist[0][0] = l[0][0]

    for i in range(n):
        for j in range(n):
            move(i, j, n, dist, visited)

    for p in dist:
        print(p)
    print()

    # print("Problem %d: %d" % (cnt, dist[n - 1][n - 1]))