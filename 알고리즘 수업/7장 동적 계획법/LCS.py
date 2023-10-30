string_a = list("HELLO WORLD")
string_b = list("GAME OVER")

def lcs_dp(x, y):
    m = len(x)
    n = len(y)
    l = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])

    return l[m][n]

result = []

def lcs_dp_traceback(x, y, l):
    lcs = ""
    i = len(x)
    j = len(y)

    while i > 0 and j > 0:
        v = l[i][j]
        if v > l[i][j - 1] and v > l[i - 1][j] and v > l[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = x[i] + lcs
        elif v == l[i][j - 1] and v > [i - 1][j]:
            j -= 1
        else:
            i -= 1
    return lcs

lcs = lcs_dp_traceback(string_a, string_b, table)
print(lcs)