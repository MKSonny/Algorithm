val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)

def knapsack(W, wt, val, n):
    a = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # 여기서 for문이 1부터 시작하는 이유는?
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                a[i][w] = a[i - 1][w]
            else:
                valWith = val[i - 1] + a[i - 1][w - wt[i - 1]]
                valWithout = a[i - 1][w]
                a[i][w] = max(valWith, valWithout)

    return a[n][W]

print(knapsack(W, wt, val, n))