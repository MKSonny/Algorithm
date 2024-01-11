from collections import deque

n = int(input())
l = []
mid = n // 2

for _ in range(n):
    l.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]
visited[mid][mid] = True

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dQ = deque()
dQ.append((mid, mid))

total = 0
total += l[mid][mid]

level = 0

while True:
    if level == n // 2:
        break

    size = len(dQ)

    for _ in range(size):
        now = dQ.popleft()

        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    total += l[ny][nx]
                    dQ.append((ny, nx))

    level += 1

print(total)
'''
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
'''