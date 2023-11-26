obj = [1, 2, 3]
def permutation(obj, sol, level, selected):
    if len(sol) == len(obj):
        print(sol)
        return

    for i in range(len(obj)):
        if not selected[i]:
            sol.append(obj[i])
            selected[i] = True
            permutation(obj, sol, level + 1, selected)
            selected[i] = False
            sol.pop()

selected = [False] * len(obj)
permutation(obj, [], 0, selected)