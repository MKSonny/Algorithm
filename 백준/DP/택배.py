n, m = map(int, input().split())
l = [[float('inf') for _ in range(n)] for _ in range(n)]
# print(l)
h = [[[] for _ in range(n)] for _ in range(n)]

for i in h:
    print(i)

for i in range(n):
    l[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    l[a - 1][b - 1] = c
    l[b - 1][a - 1] = c

for i in l:
    print(i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]
                h[i][j].append(k + 1)


for i in l:
    print(i)

for i in h:
    print(i)