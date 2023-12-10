X = "hello world"
Y = "game over"

def track(X, Y, mem):
    print("%s 를 %s로 바꾸는 과정 추적" % (X, Y))
    i = len(X)
    j = len(Y)

    while i > 0 and j > 0:
        s = min(mem[i - 1][j], mem[i - 1][j - 1], mem[i][j - 1])

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
            print("%s -> %s 로 교체" % (X[i - 1], Y[j - 1]))
            i -= 1
            j -= 1

    # Handle remaining characters
    while i > 0:
        print("%s 삭제" % X[i - 1])
        i -= 1

    while j > 0:
        print("%s 삽입" % Y[j - 1])
        j -= 1



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

    track(X, Y, mem)

    return mem[m][n]


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
            s = min(
                edit_distance(X, Y, m - 1, n, mem),
                edit_distance(X, Y, m, n - 1, mem),
                edit_distance(X, Y, m - 1, n - 1, mem)
            )
            mem[m - 1][n - 1] = s + 1

    return mem[m - 1][n - 1]


m = len(X)
n = len(Y)


edit_distance_table(X, Y)