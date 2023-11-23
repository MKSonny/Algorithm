val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
w = 18
n = len(val)

def knapsack(n, wt, val, W):
    a = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                a[i][w] = a[i - 1][w]
            else:
                valWith = val[i - 1] + a[i - 1][w - wt[i - 1]]
                valWithout = a[i - 1][w]

                a[i][w] = max(valWith, valWithout)

    return a[n][W]

print(knapsack(len(val), wt, val, w))