X = "GAME OVER"
Y = "HELLO WORLD"
print("X =", X)
print("Y =", Y)

def lcs_tracking(X, Y, table):
    i = len(X)
    j = len(Y)
    same_str = ""
    while i >= 0 and j >= 0:
        v = table[i][j]
        if v > table[i - 1][j - 1] and v > table[i][j - 1] and v > table[i - 1][j]:
            i -= 1
            j -= 1
            same_str = X[i] + same_str
        elif v > table[i - 1][j] and v == table[i][j - 1]:
            j -= 1
        else:
            i -= 1

    return same_str

def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)

    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(
                    table[i - 1][j], table[i][j - 1]
                )

    print(lcs_tracking(X, Y, table))

    return table[m][n]

print("LCS(분할 정복)", lcs_dp(X, Y))