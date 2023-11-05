val = [60, 50, 70, 30]
wt = [5, 3, 4, 2]
W = 5
n = len(val)

def knapsack_dp(W, wt, val, n):
    a = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                a[i][w] = a[i - 1][w]
            else:
                a[i][w] = max(a[i - 1][w - wt[i - 1]] + val[i - 1], a[i - 1][w])

    return a

a = knapsack_dp(W, wt, val, n)
for row in a:
    print(row)