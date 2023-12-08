def permutation(val, k, sol, selected):
    if len(sol) == k:
        print(sol)
        return

    for i in range(len(val)):
        if not selected[i]:
            sol.append(val[i])
            selected[i] = True
            # print(sol)
            permutation(val, k, sol, selected)
            selected[i] = False
            sol.pop()

permutation([1, 2, 3], 3, [], [False] * 3)
