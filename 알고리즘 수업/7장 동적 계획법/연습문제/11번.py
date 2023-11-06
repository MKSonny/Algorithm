value = [26, 20, 14, 40, 50]
weight = [3, 2, 1, 4, 5]
W = 6
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
