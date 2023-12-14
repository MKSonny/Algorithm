X = "hello world"
Y = "game over"

def edit_distance(X, Y, m, n, mem):
    if n == 0:
        return m
    if m == 0:
        return n

    if mem[m - 1][n - 1] == None:
        if X[m - 1] == Y[n - 1]:
            mem[m - 1][n - 1] = edit_distance(X, Y, m - 1, n - 1, mem)
        else:
            mem[m - 1][n - 1] = min(
                edit_distance(X, Y, m - 1, n, mem),
                edit_distance(X, Y, m, n - 1, mem),
                edit_distance(X, Y, m - 1, n - 1, mem)
            ) + 1

    return mem[m - 1][n - 1]

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                mem[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                mem[i][j] = mem[i - 1][j - 1] + 1
            else:
                mem[i][j] = max(
                    mem[i - 1][j], mem[i][j - 1]
                )

    return mem[m][n]

print(lcs(X, Y))
m, n = len(X), len(Y)
mem = [[None for _ in range(n)] for _ in range(m)]
print(edit_distance(X, Y, m, n, mem))