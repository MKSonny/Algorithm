def DFS_permutation(data, sol, level, bUsed):
    if level == len(data):
        print(sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            bUsed[i] = True
            sol.append(data[i])
            DFS_permutation(data, sol, level + 1, bUsed)
            bUsed[i] = False
            sol.pop()

DFS_permutation(list('ABC'), [], 0, [False] * 3)