X = "GAME OVER"
Y = "HELLO WORLD"

def lcs_track(X, Y, mem):
    i = len(X)
    j = len(Y)
    same_str = ""

    while i >= 0 and j >= 0:
        v = mem[i][j]
        if v > mem[i - 1][j - 1] and v > mem[i - 1][j] and v > mem[i][j - 1]:
            i -= 1
            j -= 1
            same_str = X[i] + same_str
        elif v > mem[i - 1][j] and v == mem[i][j - 1]:
            j -= 1
        else:
            i -= 1

    return same_str


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                mem[i][j] = 0
            if X[i - 1] == Y[j - 1]:
                mem[i][j] = mem[i - 1][j - 1] + 1
            else:
                mem[i][j] = max(
                    mem[i - 1][j], mem[i][j - 1]
                )

    print(lcs_track(X, Y, mem))
    return mem[m][n]

print(lcs(X, Y))