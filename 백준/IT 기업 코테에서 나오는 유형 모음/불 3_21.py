import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(list(sys.stdin.readline().rstrip()))

answer = []

'''
6 7
#######
#..J.F#
#.....#
#......
......#
#######

1. 불은 무조건 4방향으로 퍼진다.
2. 하지만 지훈이는 가장 효율적인 경로로 이동해야 한다.
3. 1분 뒤 불이 먼저 퍼지게 하고 지훈이를 움직인다.
4. 이후 지훈이 bfs
'''
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def print_board(l):
    for i in l:
        print(i)
    print()

def bfs(l, i, j, visited):
    q = deque([(i, j)])
    visited[i][j] = True
    l[i][j] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if l[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    l[ny][nx] = l[y][x] + 1
                    visited[ny][nx] = True


def final_bfs(l, i, j, visited):
    q = deque([(i, j)])
    visited[i][j] = True
    l[i][j] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if type(l[ny][nx]) is not str:
                    if l[ny][nx] > 0 and not visited[ny][nx]:
                        q.append((ny, nx))
                        l[ny][nx] = l[y][x] + 1
                        visited[ny][nx] = True


# print_board(l)

for i in range(n):
    for j in range(m):
        if l[i][j] == '.':
            l[i][j] = 0

j_board = copy.deepcopy(l)
f_board = copy.deepcopy(l)

j_position = []

for i in range(n):
    for j in range(m):
        if j_board[i][j] == 'J':
            j_position.append((i, j))
        if f_board[i][j] == 'J':
            f_board[i][j] = 0

visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if j_board[i][j] == 'J':
            bfs(j_board, i, j, visited)

# print_board(j_board)

visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if f_board[i][j] == 'F':
            bfs(f_board, i, j, visited)


# print_board(f_board)

for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            l[i][j] = f_board[i][j] - j_board[i][j]

# print_board(l)

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if l[i][j] == 'J':
            final_bfs(l, i, j, visited)


# print_board(l)


def not_string(k):
    if type(k) is not str and k > 0:
        answer.append(k)


for i in range(n):
    not_string(l[i][0])
    not_string(l[i][m - 1])

for j in range(m):
    not_string(l[0][j])
    not_string(l[n - 1][j])

if len(answer) == 0:
    print('IMPOSSIBLE')
else:
    print(min(answer) + 1)