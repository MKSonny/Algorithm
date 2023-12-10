def all_permutations(data):
    bUsed = [False] * len(data)
    permutation(data, [], 0, bUsed)

def permutation(obj, sol, level, mark):
    if level == len(obj):
        print(sol)
        return

    for i in range(len(obj)):
        if mark[i] == False:
            sol.append(obj[i])
            mark[i] = True
            permutation(obj, sol, level + 1, mark)
            sol.pop()
            mark[i] = False

obj = ['A', 'B', 'C']
all_permutations(obj)