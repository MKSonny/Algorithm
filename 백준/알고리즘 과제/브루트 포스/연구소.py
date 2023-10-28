# 한 줄씩 입력 받기
import queue

n, m = map(int, input().split())  # 첫 줄에서 두 개의 정수를 공백으로 구분하여 입력 받음

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))  # 각 줄에서 숫자들을 공백으로 구분하여 리스트로 변환
    matrix.append(row)

def combination(a):
    all_combi = []
    n = len(a)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                all_combi.append((a[i], a[j], a[k]))

    return all_combi

zeros = []
virus = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = queue.Queue()


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zeros.append((i, j))
        elif matrix[i][j] == 2:
            virus.append((i, j))

all_combi = combination(zeros, len(zeros))

prev = [[[0] for _ in range(m)] for _ in range(n)]
prev[:] = matrix[:]

def bfs(q):
    cnt = 0

    while not q.empty():
        (x, y) = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                q.put((nx, ny))


    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                cnt += 1

    return cnt

cnt = 0
max = 0
for value in all_combi:
    matrix = [row[:] for row in prev]
    wall_a, wall_b, wall_c = value[0], value[1], value[2]

    matrix[wall_a[0]][wall_a[1]] = 1
    matrix[wall_b[0]][wall_b[1]] = 1
    matrix[wall_c[0]][wall_c[1]] = 1

    for spread in virus:
        q.put((spread[0], spread[1]))

    safe_area = bfs(q)

    if max < safe_area:
        max = safe_area

print(max)