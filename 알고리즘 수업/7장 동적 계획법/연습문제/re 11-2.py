def knapsack_mem(n, w, mem, wt, val):
    if mem[n][w] == None:
        if n == 0 or w == 0:
            mem[n][w] = 0
        elif wt[n - 1] > w:
            mem[n][w] = knapsack_mem(n - 1, w, mem, wt, val)
        else:
            valWith = val[n - 1] + knapsack_mem(n - 1, w - wt[n - 1], mem, wt, val)
            valWithout = knapsack_mem(n - 1, w, mem, wt, val)
            mem[n][w] = max(valWith, valWithout)
    return mem[n][w]

val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
n = len(val)

mem = [[None for _ in range(W + 1)] for _ in range(n + 1)]

print(knapsack_mem(n, W, mem, wt, val))