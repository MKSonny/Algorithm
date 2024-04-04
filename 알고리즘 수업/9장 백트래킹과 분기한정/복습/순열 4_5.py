def all_permutation(data):
    bUsed = [False] * len(data)
    dfs_permutation(data, [], 0, bUsed)

def dfs_permutation(data, sol, level, bUsed):
    if level == len(data):
        # print(sol)
        return

    for i in range(len(data)):
        if not bUsed[i]:
            sol.append(data[i])
            bUsed[i] = True
            print(sol)
            dfs_permutation(data, sol, level + 1, bUsed)
            sol.pop()
            bUsed[i] = False

all_permutation(['A', 'B', 'C'])