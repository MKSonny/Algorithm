X = "hello world"
Y = "game over"

m = len(X)
n = len(Y)

def track(X, Y, mem):
    i = len(X) - 1
    j = len(Y) - 1

    while i > 0 and j > 0:
        s = min(mem[i - 1][j - 1], mem[i][j - 1], mem[i - 1][j])

        if s == mem[i][j]:
            i -= 1
            j -= 1
        elif s == mem[i - 1][j]:
            print("%s 삭제" % X[i - 1])
            i -= 1
        elif s == mem[i][j - 1]:
            print("%s 삽입" % Y[j - 1])
            j -= 1
        else:
            print("%s -> %s로 교체" % (X[i - 1], Y[j - 1]))
            i -= 1
            j -= 1


def edit_distance_table(X, Y):
    m = len(X)
    n = len(Y)

    mem = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                mem[i][j] = j
            elif j == 0:
                mem[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                mem[i - 1][j - 1] = mem[i - 1][j - 1]
            else:
                mem[i - 1][j - 1] = min(
                    mem[i - 1][j - 1], mem[i - 1][j], mem[i][j - 1]
                ) + 1

    for i in mem:
        print(i)
    # track(X, Y, mem)

    return mem[m - 1][n - 1]


def edit_distance(X, Y, mem, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if mem[m - 1][n - 1] == None:
        if X[m - 1] == Y[n - 1]:
            mem[m - 1][n - 1] = edit_distance(X, Y, mem, m - 1, n - 1)
        else:
            mem[m - 1][n - 1] = min(
                edit_distance(X, Y, mem, m - 1, n - 1),
                edit_distance(X, Y, mem, m, n - 1),
                edit_distance(X, Y, mem, m - 1, n),
            ) + 1

    return mem[m - 1][n - 1]


mem = [[None for _ in range(n)] for _ in range(m)]
edit_distance(X, Y, mem, m, n)
edit_distance_table(X, Y)