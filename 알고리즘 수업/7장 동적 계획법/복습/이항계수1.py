def coef(n, k):
    c = [[-1] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

    for i in c:
        print(i)

    return c[n][k]

print(coef(4, 1))