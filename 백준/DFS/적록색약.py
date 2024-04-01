import copy
import sys

n = int(input())
l = []

for i in range(n):
    l.append(list(sys.stdin.readline().rstrip()))

l2 = copy.deepcopy(l)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

colors = ['R', 'G', 'B']

cnt = 0

for c in range(3):
    q = [] # 다른 색일 때마다 다른 큐를 생성한다.
    for i in range(n):
        for j in range(n):
            if l[i][j] == colors[c]:
                # 같은 색이 있는 위치 정보를 저장한다.
                # 처음에는 'R'
                cnt += 1
                q.append((i, j))
                while q:
                    y, x = q.pop(0)
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if l[ny][nx] == colors[c]:
                                l[ny][nx] = 'E'
                                q.append((ny, nx))

print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if l2[i][j] == 'R':
            l2[i][j] = 'G'

cnt = 0

for c in range(3):
    q = [] # 다른 색일 때마다 다른 큐를 생성한다.
    for i in range(n):
        for j in range(n):
            if l2[i][j] == colors[c]:
                # 같은 색이 있는 위치 정보를 저장한다.
                # 처음에는 'R'
                q.append((i, j))
                cnt += 1
                while q:
                    y, x = q.pop(0)
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if l2[ny][nx] == colors[c]:
                                l2[ny][nx] = 'E'
                                q.append((ny, nx))

print(cnt, end=' ')
