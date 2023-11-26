obj = [1, 2, 3, 4, 5]
M = 9

def dfs(obj, M, sol, level, remaing):
    if sum(sol) == M:
        print(sol)
        return
    if remaing + sum(sol) <= M:
        print("work")
        return

    if sum(sol) > M:
        return

    for i in range(level, len(obj)):
        sol.append(obj[i])
        dfs(obj, M, sol, i + 1, remaing - obj[i])
        sol.pop()

dfs(obj, M, [], 0, sum(obj))