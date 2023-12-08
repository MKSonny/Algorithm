X = "GAME OVER"
Y = "HELLO WORLD"

def lcs_track(X, Y, table):
    i = len(X)
    j = len(Y)
    same = ""

    while i >= 0 and j >= 0:
        v = table[i][j]
        if v > table[i - 1][j - 1] and v > table[i - 1][j] and v > table[i][j - 1]:
            i -= 1
            j -= 1
            same = X[i] + same
        elif v > table[i - 1][j] and v == table[i][j - 1]:
            j -= 1
        else:
            i -= 1

    return same

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(
                    table[i - 1][j], table[i][j - 1]
                )

    print(lcs_track(X, Y, table))

    return table[m][n]

print(lcs(X, Y))