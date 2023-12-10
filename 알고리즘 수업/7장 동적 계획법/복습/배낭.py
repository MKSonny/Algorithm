val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
w = 6

def knapsack(val, wt, W, n):
    mem = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                mem[i][w] = mem[i - 1][w]
            else:
                valWith = val[i - 1] + mem[i - 1][w - wt[i - 1]]
                valWithout = mem[i - 1][w]
                mem[i][w] = max(valWith, valWithout)

    for i in mem:
        print(i)

    return mem[n][W]

print(knapsack(val, wt, w, len(val)))