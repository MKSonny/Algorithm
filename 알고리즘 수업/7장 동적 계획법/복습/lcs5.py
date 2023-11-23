X = "GAME OVER"
Y = "HELLO WORLD"
print("X =", X)
print("Y =", Y)

def lcs_track(X, Y, l):
    i = len(X)
    j = len(Y)
    str = ''

    while i >= 0 and j >= 0:
        v = l[i][j]
        if v > l[i - 1][j - 1] and v > l[i - 1][j] and v > l[i][j - 1]:
            i -= 1
            j -= 1
            str = X[i] + str
        elif v > l[i - 1][j] and v == l[i][j - 1]:
            j -= 1
        else:
            i -= 1

    print(str)

def lcs(X, Y):
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

    lcs_track(X, Y, l)
    return l[m][n]

print(lcs(X, Y))