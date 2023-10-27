import queue

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
# 토마토 받아서 넣기. 이차원 리스트로 만들어질거.
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)


def print_queue_contents(q):
    elements_copy = list(q.queue)
    for element in elements_copy:
        print(element)



cnt = 0
def bfs(q):
    q2 = queue.Queue()

    while not q.empty():
        (y, x) = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < m) and (0 <= ny < n) and matrix[ny][nx] == 0:
                matrix[ny][nx] = 1
                q2.put((ny, nx))
    print(q2.qsize())
    bfs(q2)

q = queue.Queue()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.put((i, j))
            bfs(q)

print(matrix)

print(cnt)
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''


