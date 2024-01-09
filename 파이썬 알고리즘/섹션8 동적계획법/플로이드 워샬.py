n, m = map(int, input().split())

l = [[9999 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    l[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                l[i][j] = 0
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

for i in range(n):
    for j in range(n):
        if l[i][j] == 9999:
            print('M', end=' ')
        else:
            print(l[i][j], end=' ')
    print()