def combination(S, nums, level, sol, n):
    if len(sol) == len(nums):
        # print(sol)
        return
    for i in range(level, len(nums)):
        sol.append(nums[i])
        if sum(sol) == S:
            print(sol)
        # print(sol)
        combination(S, nums, i + 1, sol, n)
        sol.pop()

combination(9, [3, 34, 4, 12, 5, 2], 0, [], 2)