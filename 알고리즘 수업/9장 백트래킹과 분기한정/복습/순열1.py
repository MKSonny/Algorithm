def DFS_permutation(data, sol, level, bUsed):
    if level == len(data):
        print(sol)
        return

    if bUsed[level] == True:
        return

    for i in range(len(data)):
        bUsed[i] = True
        sol.append(data[i])
        DFS_permutation(data, sol, level + 1, bUsed)
        bUsed[i] = False
        sol.pop()