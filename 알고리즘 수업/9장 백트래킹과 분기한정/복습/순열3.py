def permutation_dfs(nums, sol, visited):
    if len(sol) == len(nums):
        print(sol)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            sol.append(nums[i])
            permutation_dfs(nums, sol, visited)
            visited[i] = False
            sol.pop()

permutation_dfs(list('ABC'), [], [False] * 3)