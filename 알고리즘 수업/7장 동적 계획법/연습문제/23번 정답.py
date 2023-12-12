X = "hello world"
Y = "game over"

def track(X, Y, mem):
    i = len(X) - 1
    j = len(Y) - 1

    while i >= 0 and j >= 0:
        s = min(mem[i - 1][j - 1] or float('inf'), mem[i][j - 1] or float('inf'), mem[i - 1][j] or float('inf'))

        if s == mem[i][j]:
            i -= 1
            j -= 1
        else:
            if s == mem[i - 1][j]:
                print("%s 삭제" % X[i])
                i -= 1
            elif s == mem[i][j - 1]:
                print("%s 삽입" % Y[j])
                j -= 1
            else:
                print("%s -> %s로 교체" % (X[i], Y[j]))
                i -= 1
                j -= 1

def edit_distance_table(X, Y):
    m = len(X)
    n = len(Y)

    mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                mem[i][j] = j
            # 여기서 조건문 사용 주의
            elif j == 0:
                mem[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                mem[i][j] = mem[i - 1][j - 1]
            else:
                mem[i][j] = min(
                    mem[i - 1][j], mem[i - 1][j - 1], mem[i][j - 1]
                ) + 1

    # for i in mem:
    #     print(i)

    track(X, Y, mem)

    return mem[m][n]

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
                edit_distance(X, Y, mem, m, n - 1), # 삽입
                edit_distance(X, Y, mem, m - 1, n) # 삭제
            ) + 1

    print("================")
    for i in mem:
        print(i)



    return mem[m - 1][n - 1]

m = len(X)
n = len(Y)
mem = [[None for _ in range(n)] for _ in range(m)]
print(edit_distance(X, Y, mem, len(X), len(Y)))
# print(edit_distance_table(X, Y))
track(X, Y, mem)