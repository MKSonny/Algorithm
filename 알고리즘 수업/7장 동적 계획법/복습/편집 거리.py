X = "hello world"
Y = "game over"

def edit_distance(X, Y, m, n, mem):
    # for i in mem:
    #     print(i)
    # print()
    if m == 0:
        return n
    if n == 0:
        return m

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


m = len(X)
n = len(Y)

mem = [[None for _ in range(n)] for _ in range(m)]

print(edit_distance(X, Y, m, n, mem))

for i in mem:
    print(i)