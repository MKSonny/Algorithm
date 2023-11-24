X = "DATA STRUCTURE"
Y = "PYTHON ALGORITHM"
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)

    l = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])

    for i in l:
        print(i)

    return l[m][n]

print(lcs_dp(X, Y))