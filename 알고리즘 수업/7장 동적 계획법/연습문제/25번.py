def edit_distance_table(X, Y):
    m = len(X)
    n = len(Y)
    mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                mem[i][j] = j
            elif j == 0:
                mem[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                mem[i][j] = mem[i - 1][j - 1]
            else:
                mem[i][j] = min(
                    mem[i][j - 1], mem[i - 1][j - 1], mem[i - 1][j]
                ) + 1

    for i in mem:
        print(i)

    return mem[m][n]

X = "hello world"
Y = "game over"
print(edit_distance_table(X, Y))