val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
n = len(val)

def knapsack_mem(W, val, wt, n, mem):
    if mem[n][W] == None:
        if W == 0 or n == 0:
            mem[n][W] = 0
        elif wt[n - 1] > W:
            mem[n][W] = knapsack_mem(W, val, wt, n - 1, mem)
        else:
            valWith = val[n - 1] + knapsack_mem(W - wt[n - 1], val, wt, n - 1, mem)
            valWithout = knapsack_mem(W, val, wt, n - 1, mem)
            return max(valWith, valWithout)

    return mem[n][W]

def do_knapsack(W, val, n, wt):
    mem = [[None for _ in range(W + 1)] for _ in range(n + 1)]
    return knapsack_mem(W, val, wt, n, mem)

print(do_knapsack(W, val, n, wt))