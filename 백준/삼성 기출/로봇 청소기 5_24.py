import sys

n, m = map(int, sys.stdin.readline().split())
start_y, start_x, direction = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

for i in l:
    print(i)

# 반시계 방향
# up, left, down, right
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

'''
5 5
2 2 1
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''

def slice_end(d):
    return (dy[-d:] + dy[0:4 - d], dx[-d:] + dx[0:4 - d])

by_direction_dy = [[-1, 0, 1, 0]]
by_direction_dx = [[0, -1, 0, 1]]

for i in range(1, 4):
    a, b = slice_end(i)
    by_direction_dy.append(a)
    by_direction_dx.append(b)

# print(by_direction_dy)
# print(by_direction_dx)
'''
만약 d가 0이라면 북쪽을 바라보고 있으므로 
순서가 기존이랑 같음
d가 1인 경우 동쪽을 바라보고 있으므로
동 -> 북 -> 서 -> 남 순서로 주변 확인
'''

cnt = 0
print()

def dfs(y, x, d):
    l[y][x] = 1

    # for i in l:
    #     print(i)
    # print()

    global cnt
    cnt += 1
    for i in range(4):
        ny = y + by_direction_dy[d][i]
        nx = x + by_direction_dx[d][i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == 0:
                if d - i == -1:
                    d = 3
                elif d - i == -2:
                    d = 2
                dfs(ny, nx, d)

dfs(start_y - 1, start_x - 1, 1)

print()
print(cnt)
print()

for i in l:
    print(i)


