nums = [3, 34, 4, 12, 5, 2]
M = 9

def combination(M, obj, level, sol, remaining):
    if len(sol) == len(obj):
        # print(sol)
        return

    if sum(sol) > M or remaining + sum(sol) < M:
        return

    if sum(sol) == M:
        print(sol)
        return

    for i in range(level, len(obj)):
        sol.append(obj[i])
        combination(M, obj, i + 1, sol, remaining - obj[i])
        sol.pop()

combination(M, nums, 0, [], sum(nums))