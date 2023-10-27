import queue

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
zero_cnt = 0
in_zero = 0
q = queue.Queue()

while not q.empty():
    zero_cnt += q.qsize()
    for i in range(q.qsize()):
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if (0 <= nx < m) and (0 <= ny < n) and (nx, ny) and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                q.put((ny, nx))

    cnt += 1

visited = set()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.put((i, j))
        elif matrix[i][j] == 0:
            in_zero += 1

if zero_cnt != in_zero:
    cnt = -1

print(cnt)


