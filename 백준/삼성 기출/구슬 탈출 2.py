n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input().strip()))

mark = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
maxx = -1

def re_(y, x, by, bx):
    # 한 dy, dx마다 blue도 들어가는지 검사
    global cnt
    global maxx

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == '.':
                result = blue(by, bx, i)
                # print(result, i)
                # print(ny, nx) # 1, 3
                cnt += 1
                print('cnt', cnt)
                maxx = max(maxx, cnt)
                if result == (-1, -1):
                    print(-1)
                    maxx = -1
                    return
                else:
                    if l[ny][nx] == 'O':
                        # print(1)
                        # maxx = 1
                        return
                    if i == 0:
                        while l[ny][nx] != '#' and l[ny][nx] == '.':
                            l[ny][nx] = ';)'
                            ny -= 1
                        re_(ny + 1, nx, result[0], result[1])
                    elif i == 1:
                        while l[ny][nx] != '#' and l[ny][nx] == '.':
                            l[ny][nx] = ';)'
                            ny += 1
                        re_(ny - 1, nx, result[0], result[1])
                    elif i == 2:
                        while l[ny][nx] != '#' and l[ny][nx] == '.':
                            l[ny][nx] = ';)'
                            nx -= 1
                        re_(ny, nx + 1, result[0], result[1])
                    elif i == 3:
                        while l[ny][nx] != '#' and l[ny][nx] == '.':
                            l[ny][nx] = ';)'
                            nx += 1
                        re_(ny, nx - 1, result[0], result[1])
    cnt -= 1

def re_v2(y, x, by, bx):
    # 한 dy, dx마다 blue도 들어가는지 검사
    global cnt
    global maxx

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == '.':
                if l[ny][nx] == 'O':
                    # print(1)
                    # maxx = 1
                    return
                if i == 0:
                    while l[ny][nx] != '#' and l[ny][nx] == '.':
                        l[ny][nx] = ';)'
                        ny -= 1
                    re_(ny + 1, nx, result[0], result[1])
                elif i == 1:
                    while l[ny][nx] != '#' and l[ny][nx] == '.':
                        l[ny][nx] = ';)'
                        ny += 1
                    re_(ny - 1, nx, result[0], result[1])
                elif i == 2:
                    while l[ny][nx] != '#' and l[ny][nx] == '.':
                        l[ny][nx] = ';)'
                        nx -= 1
                    re_(ny, nx + 1, result[0], result[1])
                elif i == 3:
                    while l[ny][nx] != '#' and l[ny][nx] == '.':
                        l[ny][nx] = ';)'
                        nx += 1
                    re_(ny, nx - 1, result[0], result[1])
    cnt -= 1

def blue(y, x, option):
    ny = y + dy[option]
    nx = x + dx[option]
    if 0 <= ny < n and 0 <= nx < m:
        if l[ny][nx] == '.':
            if option == 0:
                while l[ny][nx] != '#' and l[ny][nx] == '.':
                    ny -= 1
                    if l[ny][nx] == 'O':
                        return (-1, -1)
                return (ny + 1, nx)
            elif option == 1:
                while l[ny][nx] != '#' and l[ny][nx] == '.':
                    ny += 1
                    if l[ny][nx] == 'O':
                        return (-1, -1)
                return (ny - 1, nx)
            elif option == 2:
                while l[ny][nx] != '#' and l[ny][nx] == '.':
                    nx -= 1
                    if l[ny][nx] == 'O':
                        return (-1, -1)
                return (ny, nx + 1)
            elif option == 3:
                while l[ny][nx] != '#' and l[ny][nx] == '.':
                    nx += 1
                    if l[ny][nx] == 'O':
                        return (-1, -1)
                return (ny, nx - 1)
        else:
            return (y, x)


def dfs(y, x, k):
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if l[ny][nx] == 'O':
                if cnt > 10:
                    print(-1)
                    return
                print(cnt)
            if l[ny][nx] == '.':
                if k != i:
                    cnt += 1
                l[ny][nx] = ';)'
                # print(cnt)
                dfs(ny, nx, i)
                cnt -= 1

for i in range(n):
    for j in range(m):
        if l[i][j] == 'R':
            red_spot = (i, j)
            l[i][j] = '.'
        elif l[i][j] == 'B':
            blue_spot = (i, j)
            l[i][j] = '.'


re_(red_spot[0], red_spot[1], blue_spot[0], blue_spot[1])

# for i in l:
#     print(i)

print('res', maxx)