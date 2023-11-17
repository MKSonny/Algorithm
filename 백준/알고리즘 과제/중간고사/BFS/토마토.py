import queue

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
zero_cnt = 0

def bfs(q):
    global cnt
    global zero_cnt

    if q.qsize() == 0:
        cnt -= 1
        return
    q2 = queue.Queue()
    cnt += 1

    while not q.empty():
        (y, x) = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < m) and (0 <= ny < n) and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                zero_cnt += 1
                q2.put((ny, nx))
    bfs(q2)

q = queue.Queue()

in_zero = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.put((i, j))
        elif matrix[i][j] == 0:
            in_zero += 1
bfs(q)

if zero_cnt != in_zero:
    cnt = -1

print(cnt)
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''


