import sys

n, m = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

def spin(temp):
    return [list(reversed(col)) for col in zip(*temp)]

def mirror(temp):
    for i in range(len(temp)):
        temp[i] = temp[i][::-1]
    return temp

# l = spin(l)
# print()
# for i in l:
#     print(i)

def dfs(temp, y, x, cnt):
    cnt += 1
    global t
    if x > m - 1 or y > n - 1:
        return False
    # print(temp[y][x], end=' ')
    t += temp[y][x]
    if cnt == 4:
        return True
    return dfs(temp, y, x + 1, cnt)

def dfs_box(temp, y, x, cnt):
    cnt += 1
    global t
    if x > m - 1 or y > n - 1:
        return False
    # print(temp[y][x], end=' ')
    t += temp[y][x]
    if cnt == 4:
        return True
    if cnt % 2 == 0:
        return dfs_box(temp, y + 1, x - 1, cnt)
    else:
        return dfs_box(temp, y, x + 1, cnt)

def dfs_thunder(temp, y, x, cnt):
    cnt += 1
    global t
    if x > m - 1 or y > n - 1:
        return False
    # print(temp[y][x], end=' ')
    t += temp[y][x]
    if cnt == 4:
        return True
    if cnt == 1:
        return dfs_thunder(temp, y + 1, x, cnt)
    elif cnt == 2:
        return dfs_thunder(temp, y, x + 1, cnt)
    elif cnt == 3:
        return dfs_thunder(temp, y + 1, x, cnt)

def dfs_l(temp, y, x, cnt):
    cnt += 1
    global t
    if x > m - 1 or y > n - 1:
        return False
    # print(temp[y][x], end=' ')
    t += temp[y][x]
    if cnt == 4:
        return True
    if cnt == 3:
        return dfs_l(temp, y, x + 1, cnt)
    else:
        return dfs_l(temp, y + 1, x, cnt)

def dfs_final(temp, y, x, cnt):
    cnt += 1
    global t
    if x > m - 1 or y > n - 1:
        return False
    # print(temp[y][x], end=' ')
    t += temp[y][x]
    if cnt == 4:
        return True
    if cnt == 3:
        return dfs_final(temp, y + 1, x - 1, cnt)
    else:
        return dfs_final(temp, y, x + 1, cnt)

maxx = -1

for _ in range(2):
    for k in range(4):
        for i in range(n):
            for j in range(m):
                t = 0
                if dfs(l, i, j, 0):
                    maxx = max(maxx, t)
                    # print('t', t)
                t = 0
                if dfs_box(l, i, j, 0):
                    maxx = max(maxx, t)
                    # print('t', t)
                t = 0
                if dfs_thunder(l, i, j, 0):
                    maxx = max(maxx, t)
                    # print('t', t)
                t = 0
                if dfs_l(l, i, j, 0):
                    maxx = max(maxx, t)
                    # print('t', t)
                    # print()
                t = 0
                if dfs_final(l, i, j, 0):
                    maxx = max(maxx, t)
                t = 0
        # print(maxx)
        l = spin(l)
        n, m = m, n
    l = mirror(l)
print(maxx)