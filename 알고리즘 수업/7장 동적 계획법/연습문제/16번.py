def lcs_mem(X, Y, m, n,mem):

    for i in mem:
        print(i)
    print()

    if mem[m][n] == None:
        if m == 0 or n == 0:
            mem[m][n] = 0
        elif X[m - 1] == Y[n - 1]:
            mem[m][n] = lcs_mem(X, Y, m - 1, n - 1, mem) + 1
        else:
            mem[m][n] = max(lcs_mem(X, Y, m - 1, n, mem),
                            lcs_mem(X, Y, m, n - 1, mem)
                            )
    return mem[m][n]

def do_lcs_mem(X, Y):
    m = len(X)
    n = len(Y)

    mem = [[None for _ in range(n + 1)] for _ in range(m + 1)]
    answer = lcs_mem(X, Y, m, n, mem)
    # for i in mem:
    #     print(i)
    return answer

X = "HELLO WORLD"
Y = "GAME OVER"

print(do_lcs_mem(X, Y))