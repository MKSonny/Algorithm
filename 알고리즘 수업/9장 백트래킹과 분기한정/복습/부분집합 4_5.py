val = [1, 2, 3]
n = 3
def combination(val, n, sol, level):
    for i in range(level, n):
        sol.append(val[i])
        print(sol)
        combination(val, n, sol, i + 1)
        sol.pop()

combination(val, n, [], 0)