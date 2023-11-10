def all_sum_of_subsets(S, M):
    DFS_sum_of_subsets(S, M, 0, [], sum(S))


def DFS_sum_of_subsets(S, M, level, sol, remaining):
    if sum(sol) == M:
        print(sol)
        return

    if sum(sol) > M or (remaining + sum(sol)) < M:
        return

    # 여기 for문의 역할을 이해해야 한다..
    # 어떻게 첫번째 dfs에는 하나의 요소만 있고
    # 두번째 dfs에는 2개의 요소가 있는지..

    # 그냥 반복문만 사용했으면
    # 여기서 재귀를 사용한 이유는 반복문을 통해 원소를 추가할 때
    # 해당 원소를 넣어도 되는지 확인한다.
    # 3은 그래로 유지하고 다음 원소를 확인하고 싶어서?
    # 이기적으로 나는 계속 유지하고 싶으니까

    # 조건을 만족한다면 각 dfs는 for문을 수행한다.
    # level 이상 부터
    # 근데 dfs가 방해해서 for문을 한번밖에 못돈다.
    # for문은 append가 중심이 아니라 다양성이 중심이다.
    for i in range(level, len(S)):
        # [3, 4]에서 [3, 4, 5]로 되고 dfs
        # 조건 만족하지 않으므로 return
        # [3, 4]에서 여기에 [3, 4, 5]있는데 이거
        # [3, 4]는 기본적으로 유지해야한다.
        # 되는지 확인해주세요, 하고 넘김
        # 근데 어 이거 안되요 그러면
        # 아 그래요 그럼 [3, 4, 2] 이거는 되는지 확인해주세요
        # 넘겨주고 어 되네
        sol.append(S[i])
        # 만약 계속 맞는 조건이 되면 pop을 안 할 것이다.
        DFS_sum_of_subsets(S, M, i + 1, sol, remaining - S[i])
        # 합이 9가 아니면 마지막을 버린다..
        # 어디서?
        sol.pop()

nums = [3, 34, 4, 12, 5, 2]
M = 9
solution = all_sum_of_subsets(nums, M)
print("입력 집합:", nums, "M =", M)