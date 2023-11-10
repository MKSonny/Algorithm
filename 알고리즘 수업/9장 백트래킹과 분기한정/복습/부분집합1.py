def subsets(M, level, sol, data, remaining):
    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) > M or sum(sol) + remaining < M:
        return

    for i in range(level, len(data)):
        sol.append(data[i])
        subsets(M, i + 1, sol, data, remaining - data[i])
        sol.pop()

nums = [3, 34, 4, 12, 5, 2]
M = 9
subsets(M, 0, [], nums, sum(nums))