n = int(input())

bag_3kg = 3
bag_5kg = 5

# def dfs_track(table, n):


def to_knapsack_dp(wt, n):
    A = [[0 for _ in range(n + 1)] for _ in range(2 + 1)]
    count_3 = 0
    count_5 = 0
    before = -1

    for i in range(1, 2 + 1):
        for w in range(1, n + 1):
            if wt[i - 1] > w:
                A[i][w] = A[i - 1][w]
            else:
                # 이전 물건을 뺄 필요가 없으므로 기존
                # knapsack 문제에서는
                # valWith = wt[i - 1] + A[i - 1][w - wt[i - 1]]
                # 현재는 아래와 같이 해야 한다.
                valWith = wt[i - 1] + A[i][w - wt[i - 1]]
                valWithout = A[i - 1][w]

                for_count = max(valWith, valWithout)
                A[i][w] = for_count

    if A[2][n] != n:
        return -1

    for i in A:
        print(i)

    print(3, count_3)
    print(5, count_5)

to_knapsack_dp([3, 5], n)