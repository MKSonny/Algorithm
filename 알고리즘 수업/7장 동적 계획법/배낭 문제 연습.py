def knapsack_dp(w, wt, val, n):
    A = [[0 for x in range(w + 1)] for x in range(n + 1)]

    for i in range(1, w + 1):
        for w in range(1, n + 1):
            # 더하게 될 값이 총 무게보다 많이 나갈 경우
            if wt[i - 1] > w:

