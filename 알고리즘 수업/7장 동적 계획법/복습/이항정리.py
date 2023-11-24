def bin_coef(n, k):
    c = [[0 for _ in range(k)] for _ in range(n)]

    for i in range(n):
        for j in range(min(i, k) + 1):
            if i == j:
                c[i][j] = 1
            else:
                c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

    return c[n][k]

bin_coef(4, 2)