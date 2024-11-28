import sys
from itertools import product
import copy

N, M = map(int, sys.stdin.readline().split())
l = [list(map(int, input().split())) for _ in range(N)]

multi = [
    [1, 2, 3, 4],
    [5, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14],
    [15]
]

one = [1, 2, 3, 4]
two = [5, 6]
three = [7, 8, 9, 10]
four = [11, 12, 13, 14]
five = [15]

def cc(y, x, option, t_l):
    if option == 1 or option == 5 or option == 7 or option == 10 or option == 11 or option == 12 or option == 14 or option == 15:
        # 위
        for i in range(y - 1, -1, -1):
            if t_l[i][x] == 6:
                break
            t_l[i][x] = '#'
    if option == 2 or option == 5 or option == 8 or option == 9 or option == 12 or option == 13 or option == 14 or option == 15:
        # 아래
        for i in range(y + 1, N):
            if t_l[i][x] == 6:
                break
            t_l[i][x] = '#'
    if option == 3 or option == 6 or option == 7 or option == 8 or option == 11 or option == 12 or option == 13 or option == 15:
        # 오른쪽
        for i in range(x + 1, M):
            if t_l[y][i] == 6:
                break
            t_l[y][i] = '#'
    if option == 4 or option == 6 or option == 9 or option == 10 or option == 11 or option == 13 or option == 14 or option == 15:
        # 왼쪽
        for i in range(x - 1, -1, -1):
            if t_l[y][i] == 6:
                break
            t_l[y][i] = '#'

t = []

# 1, 2, 3, 4
# 5, 6
mem = []
for i in range(len(l)):
    for j in range(len(l[0])):
        if 1 <= l[i][j] <= 5:
            mem.append((i, j))
            t.append(multi[l[i][j] - 1])

p = product(*t)

def count_zero(li):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if li[i][j] == 0:
                cnt += 1
    return cnt

minn = float('inf')

for idx, i in enumerate(p):
    t_l = copy.deepcopy(l)
    for k, j in enumerate(i):
        cc(mem[k][0], mem[k][1], j, t_l)

    minn = min(count_zero(t_l), minn)

print(minn)