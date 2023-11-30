val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
n = len(val)

def knapsack(wt, val, w, n, mem):
    if mem[n][w] == None:
        if w == 0 or n == 0:
            mem[n][w] = 0
        elif wt[n - 1] > w:
            mem[n][w] = knapsack(wt, val, w, n - 1, mem)
        else:
            valWith = val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1, mem)
            valWithout = knapsack(wt, val, w, n - 1, mem)
            mem[n][w] = max(valWith, valWithout)
    return mem[n][w]

def do_knapsack(wt, val, w, n):
    mem = [[None for _ in range(w + 1)] for _ in range(n + 1)]

    return knapsack(wt, val, w, n, mem)

print(do_knapsack(wt, val, W, n))