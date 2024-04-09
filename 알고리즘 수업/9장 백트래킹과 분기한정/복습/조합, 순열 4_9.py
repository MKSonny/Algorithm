def combination(l, sol, level, k):
    if len(sol) == k:
        print(sol)
        return
    for i in range(level, len(l)):
        sol.append(l[i])
        combination(l, sol, i + 1, k)
        sol.pop()

l = ['A', 'B', 'C']
combination(l, [], 0, 2)