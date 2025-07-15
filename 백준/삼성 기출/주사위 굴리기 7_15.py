import sys
from collections import deque

n, m, y, x, o = map(int, sys.stdin.readline().split())

l = [[] for _ in range(n)]

for i in range(n):
    l[i] = list(map(int, sys.stdin.readline().split()))

orders = list(map(int, sys.stdin.readline().split()))

col_q = [0, 0, 0, 0]
row_q = [0, 0, 0]

d_col_q = deque(col_q)
d_row_q = deque(row_q)

def check(l, y, x, num, d):
    if l[y][x] == 0:
        l[y][x] = num
        d_col_q[-1] = l[y][x]
    else:
        d_col_q[-1] = l[y][x]
        l[y][x] = 0


m -= 1
n -= 1

for i in orders:
    if i == 4:
        if y + 1 > n:
            continue
        y += 1

        d_col_q.appendleft(d_col_q.pop())

        check(l, y, x, d_col_q[-1], d_col_q)
        # d_col_q[-1] = l[y][x]
        d_row_q[1] = d_col_q[1]
    elif i == 3:
        if y - 1 < 0:
            continue
        y -= 1

        d_col_q.append(d_col_q.popleft())

        check(l, y, x, d_col_q[-1], d_col_q)
        # d_col_q[-1] = l[y][x]
        d_row_q[1] = d_col_q[1]
    elif i == 2:
        if x - 1 < 0:
            continue
        x -= 1


        d_row_q.append(d_col_q.pop())
        d_col_q.append(d_row_q.popleft())

        check(l, y, x, d_col_q[-1], d_col_q)
        # d_col_q[-1] = l[y][x]
        d_col_q[1] = d_row_q[1]
    else:
        if x + 1 > m:
            continue
        x += 1



        d_row_q.appendleft(d_col_q.pop())
        d_col_q.append(d_row_q.pop())

        check(l, y, x, d_col_q[-1], d_col_q)
        # d_col_q[-1] = l[y][x]
        d_col_q[1] = d_row_q[1]

    # l[y][x] = 0
    print(d_col_q[1])
