nums = [3, 34, 4, 12, 5, 2]
M = 9

def combination(M, sol, nums, level, remaining):
    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) + remaining < M or sum(sol) > M:
        return

    for i in range(level, len(nums)):
        sol.append(nums[i])
        combination(M, sol, nums, i + 1, remaining - nums[i])
        sol.pop()

combination(M, [], nums, 0, sum(nums))