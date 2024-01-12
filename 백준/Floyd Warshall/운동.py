import sys

input = sys.stdin.readline

n, m = map(int, input().split())

l = [[10000*800 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    l[a - 1][b - 1] = c

for i in range(n):
    for j in range(n):
        if i == j:
            l[i][j] = 0


for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

minn = 10000*800

# for i in l:
#     print(i)


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if minn > l[i][j] + l[j][i]:
            minn = l[i][j] + l[j][i]



if minn >= 10000*800:
    print(-1)
else:
    print(minn)