def combination_dfs(nums, level, sol, n, result):
    if len(sol) == n:
        print(sol)
        result.append(sol.copy())
        return

    for i in range(level, len(nums)):
        sol.append(nums[i])
        combination_dfs(nums, i + 1, sol, n, result)
        sol.pop()

result = []
combination_dfs([1, 2, 3, 4, 5], 0, [], 2, result)
print(len(result))