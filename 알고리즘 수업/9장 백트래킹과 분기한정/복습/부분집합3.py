def combination(val, level, sol, k):
    if len(sol) == k:
        print(sol)
        return

    for i in range(level, len(val)):
        sol.append(val[i])
        combination(val, i + 1, sol, k)
        sol.pop()

combination([1, 2, 3], 0, [], 2)