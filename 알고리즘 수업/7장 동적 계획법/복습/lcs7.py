X = "GAME OVER"
Y = "HELLO WORLD"
print("X =", X)
print("Y =", Y)

def lcs_track(X, Y, a):
    i = len(X)
    j = len(Y)
    same = ""

    while i >= 0 and j >= 0:
        v = a[i][j]
        if v > a[i - 1][j - 1] and v > a[i - 1][j] and v > a[i][j - 1]:
            i -= 1
            j -= 1
            same = X[i] + same
        elif v > a[i - 1][j] and v == a[i][j]:
            j -= 1
        else:
            i -= 1
    return same

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    a = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                a[i][j] = a[i - 1][j - 1] + 1
            else:
                a[i][j] = max(
                    a[i - 1][j], a[i][j - 1]
                )
    print(lcs_track(X, Y, a))

    return a[m][n]

print(lcs(X, Y))