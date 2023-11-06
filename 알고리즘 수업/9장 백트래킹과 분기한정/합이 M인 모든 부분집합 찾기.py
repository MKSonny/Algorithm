def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S, M, 0, [], sum(S))


def DFS_sum_of_subsets(S, M, level, sol, remaining):
    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) > M or (remaining + sum(sol)) < M:
        return

    for i in range(level, len(S)):
        sol.append(S[i])
        DFS_sum_of_subsets(S, M, i + 1, sol, remaining - S[i])
        sol.pop()

nums = [3, 34, 4, 12, 5, 2]
M = 9
solution = all_sum_of_subsets(nums, M)
print("입력 집합:", nums, "M =", M)