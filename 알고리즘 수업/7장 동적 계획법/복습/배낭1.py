def knapsack(val, wt, W):
    mem = [[0 for _ in range(W + 1)] for _ in range(len(val) + 1)]

    for i in range(len(val) + 1):
        for w in range(W + 1):
            if wt[i - 1] > w:
                mem[i][w] = mem[i - 1][w]
            else:
                valWith = val[i - 1] + mem[i - 1][w - wt[i - 1]]
                valWithout = mem[i - 1][w]
                mem[i][w] = max(valWith, valWithout)

    return mem[len(val)][W]

def knapsack_mem(val, wt, mem, n, w):
    if n == 0 or w == 0:
        mem[n][w] = 0
    if mem[n][w] == None:
        if wt[n - 1] > w:
            mem[n][w] = knapsack_mem(val, wt, mem, n - 1, w)
        else:
            valWith = val[n - 1] + knapsack_mem(val, wt, mem, n - 1, w - wt[n - 1])
            valWithout = knapsack_mem(val, wt, mem, n - 1, w)
            mem[n][w] = max(valWith, valWithout)

    return mem[n][w]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18

print(knapsack(val, wt, W))

mem = [[None for _ in range(W + 1)] for _ in range(len(val) + 1)]
print(knapsack_mem(val, wt, mem, len(val), W))
for i in mem:
    print(i)