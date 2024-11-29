import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

how = []

for _ in range(m):
    how.append(list(map(int, sys.stdin.readline().split())))

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 1. 시작점을 기준으로만 움직여도 됨 -> 모든 죄표를 리스트에 저장
# 1). num은 dy[i] + num 이렇게
# 2. 1씩 증가
# 3. 대각선 검사
# 4. 구름있던 칸 제외, 2이상인 곳 검사
# 5. 2씩 감소
# 6.

l = [[(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]]

# for i in board:
#     print(i)
# print()

c_dy = [-1, 1, -1, 1]
c_dx = [-1, 1, 1, -1]

# 대각선 확인
def check(y, x):
    cnt = 0
    for i in range(4):
        ny = y + c_dy[i]
        nx = x + c_dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
            cnt += 1
    return cnt

# 이동


# for i in board:
#     print(i)
# print()

def bfs(y, x, visited):
    q = deque([(y, x)])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    temp = []
    while q:
        y, x = q.popleft()
        temp.append((y, x))
        board[y][x] -= 2
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and board[ny][nx] >= 2:
                    q.append((ny, nx))
    return temp


def rain(l, d, num):
    temp = []

    for y, x in l:
        ny = (y + (dy[d - 1] * num)) % n
        nx = (x + (dx[d - 1] * num)) % n
        # print(ny, nx)
        board[ny][nx] += 1
        # 좌표 수정


        temp.append((ny, nx))

        for y, x in temp:
            board[y][x] += check(y, x)
            visited[y][x] = True

    for i in board:
        print(i)
    print()


t = []

for d, num in how:
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in l:
        rain(i, d, num)



    l = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not visited[i][j]:
                l.append(bfs(i, j, visited))

for i in board:
    print(i)