nums = [1, 2, 3, 4]
M = 9

def combination(nums, sol, level):
    if len(sol) == len(nums):
        return

    for i in range(level, len(nums)):
        sol.append(nums[i])
        print(sol)
        combination(nums, sol, i + 1)
        sol.pop()

combination(nums, [], 0)