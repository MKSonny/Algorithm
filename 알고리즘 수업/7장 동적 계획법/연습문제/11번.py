val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
n = len(val)

mem = [[None for _ in range(W + 1)] for _ in range(n + 1)]

def knapsack_dp(W, wt, val, n):
    table = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                table[i][w] = table[i - 1][w]
            else:
                valWith = val[i - 1] + table[i - 1][w - wt[i - 1]]
                valWithout = table[i - 1][w]
                table[i][w] = max(valWith, valWithout)

    return table[n][w]

def knapsack_mem(W, wt, val, n, mem):
    if mem[n][W] == None:
        if n == 0 or W == 0:
            mem[n][W] = 0
        elif wt[n - 1] > W:
            mem[n][W] = knapsack_mem(W, wt, val, n - 1, mem)
        else:
            valWith = val[n - 1] + knapsack_mem(W - wt[n - 1], wt, val, n - 1, mem)
            valWithout = knapsack_mem(W, wt, val, n - 1, mem)
            mem[n][W] = max(valWith, valWithout)

    return mem[n][W]

print(knapsack_mem(W, wt, val, n, mem))
print(knapsack_dp(W, wt, val, n))