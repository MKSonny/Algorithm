def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    for i in range(m + 1):
        print(L[i])
    print("LCS =", lcs_dp_traceback(X, Y, L))

    return L[m][n]


def lcs_dp_traceback(X, Y, L):
    lcs = ''
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs

        elif v == L[i][j - 1] and v > L[i - 1][j]:
            j -= 1
        else:
            i -= 1

    return lcs

Xr = "GAME OVER"
Y = "HELLO WORLD"
print("X =", X)
print("Y =", Y)
print("LCS(분할 정복)", lcs_dp(X, Y))