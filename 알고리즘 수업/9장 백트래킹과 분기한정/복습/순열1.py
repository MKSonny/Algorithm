def DFS_permutation(nums, sol, selected):
    if len(sol) == len(nums):
        print(sol)
        return

    for i in range(len(nums)):
        if not selected[i]:
            selected[i] = True
            sol.append(nums[i])
            # print(sol)
            DFS_permutation(nums, sol, selected)
            selected[i] = False
            sol.pop()

DFS_permutation(list('ABC'), [], [False] * 3)