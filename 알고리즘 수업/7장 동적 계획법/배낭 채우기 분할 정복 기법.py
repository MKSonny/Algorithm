def knapsack_bf(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapsack_bf(W, wt, val, n - 1)
    else:
        valWithout = knapsack_bf(W, wt, val, n - 1)
        valWith = val[n - 1] + knapsack_bf(W - wt[n - 1], wt, val, n - 1)
        return max(valWith, valWithout)