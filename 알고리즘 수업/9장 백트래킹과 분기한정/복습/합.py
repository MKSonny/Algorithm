nums = [3, 34, 4, 12, 5, 2]
M = 9

def subsets(nums, sol, level, M, remaing):
    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) > M or M > remaing + sum(sol):
        return

    for i in range(level, len(nums)):
        sol.append(nums[i])
        subsets(nums, sol, i + 1, M, remaing - nums[i])
        sol.pop()

subsets(nums, [], 0, M, sum(nums))