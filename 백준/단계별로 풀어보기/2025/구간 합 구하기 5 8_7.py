import sys

a, b = map(int, sys.stdin.readline().split())

l = []

for _ in range(a):
    l.append(list(map(int, sys.stdin.readline().split())))


for i in range(a):
    t = l[i][0]
    for j in range(1, a):
        # l[i][j] += t
        t += l[i][j]
        l[i][j] = t

t = []

for _ in range(b):
    a, b, c, d = map(int, sys.stdin.readline().split())
    t.append((a - 1, b - 1, c - 1, d - 1))



def p():
    for i in l:
        print(i)

p()

for y1, x1, y2, x2 in t:
    a = 0

    # print(x1, y1, x2, y2)
    # print(l[y1][x1 - 1])
    # print(l[y2][x1 - 1])

    if x1 > 0:
        for i in range(y1, y2 + 1):
            a -= l[i][x1 - 1]

    for i in range(y1, y2 + 1):
        a += l[i][x2]

    # print(l[y1][x2])
    # print(l[y2][x2])

    print(a)
    # print()