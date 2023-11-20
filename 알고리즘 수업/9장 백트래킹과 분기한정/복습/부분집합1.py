nums = [3, 34, 4, 12, 5, 2]
M = 9

def subsets(S, M, sol, level, remaining):

    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) > M or remaining + sum(sol) < M:
        return

    for i in range(level, len(S)):
        sol.append(S[i])
        subsets(S, M, sol, i + 1, remaining - S[i])
        sol.pop()

subsets(nums, M, [], 0, sum(nums))