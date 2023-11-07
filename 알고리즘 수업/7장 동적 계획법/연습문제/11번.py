value = [26, 20, 14, 40, 50]
weight = [3, 2, 1, 4, 5]
W = 6

C = [[None for _ in range(W + 1)] for _ in range(len(value) + 1)]

def knapSack_mem(W, wt, val, n):
    if C[n][W] == None:
        if n == 0 or W == 0:
            C[n][W] = 0
    else:
        if wt[n - 1] > W:
            return C[n - 1][W]
        else:
            valWithout = knapSack_bf(W, wt, val, n - 1)
            valWith = knapSack_bf(W - wt[n - 1], wt, val, n - 1) + val[n - 1]
            return max(valWith, valWithout)


def knapSack_bf(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapSack_bf(W, wt, val, n - 1)
    else:
        valWithout = knapSack_bf(W, wt, val, n - 1)
        valWith = knapSack_bf(W - wt[n - 1], wt, val, n - 1) + val[n - 1]
        return max(valWith, valWithout)


def knapsack_dp(value, weight, W):
    a = [[0 for _ in range(W + 1)] for _ in range(len(value) + 1)]

    for i in range(1, len(value) + 1):
        for w in range(1, W + 1):
            if weight[i - 1] > w:
                a[i][w] = a[i - 1][w]
            else:
                valueWith = a[i - 1][w - weight[i - 1]] + value[i - 1]
                valueWithout = a[i - 1][w]
                a[i][w] = max(valueWith, valueWithout)

    return a[len(value)][W]

print(knapsack_dp(value, weight, W))
