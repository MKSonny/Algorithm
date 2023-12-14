nums = [1, 2, 3, 4]
M = 9

def com(nums, M, sol, level):
    if sum(sol) == M:
        print(sol)
        return

    for i in range(level, len(nums)):
        sol.append(nums[i])
        com(nums, M, sol, i + 1)
        sol.pop()

com(nums, M, [], 0)
