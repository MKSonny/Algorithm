val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
w = 18

def knapsack(val, wt, n, w, mem):

    if mem[n][w] == None:
        if n == 0 or w == 0:
            mem[n][w] = 0

        elif wt[n - 1] > w:
            mem[n][w] = knapsack(val, wt, n - 1, w, mem)
        else:
            valWith = val[n - 1] + knapsack(val, wt, n - 1, w - wt[n - 1], mem)
            valWithout = knapsack(val, wt, n - 1, w, mem)
            mem[n][w] = max(valWith, valWithout)

    return mem[n][w]

n = len(val)
mem = [[None for _ in range(w + 1)] for _ in range(len(val) + 1)]
print(knapsack(val, wt, n, w, mem))
for i in mem:
    print(i)