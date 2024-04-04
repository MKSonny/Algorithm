val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)

def dp_knapsack(val, wt, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                valWith = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                valWithout = dp[i - 1][w]
                dp[i][w] = max(valWith, valWithout)

    return dp[n][w]

'''
[0, 0, 60, 60, 120, 120, 180, 180, 190, 220, 250, 280, 310, 310, 370, 370, 370, 410, 410]
[0, 0, 60, 60, 120, 120, 180, 200, 200, 260, 260, 320, 320, 380, 380, 390, 420, 450, 480]
[0, 0, 60, 60, 120, 120, 180, 200, 210, 260, 270, 320, 330, 380, 380, 410, 420, 470, 480]
'''
print(dp_knapsack(val, wt, W, n))
