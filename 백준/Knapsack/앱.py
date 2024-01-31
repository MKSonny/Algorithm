import sys

n, W = map(int, sys.stdin.readline().split())
wt = list(map(int, sys.stdin.readline().split()))
val = list(map(int, sys.stdin.readline().split()))

mem = [[None for _ in range(W + 1)] for _ in range(n + 1)]

# 지금은 없는 상태에서 넣은 것, 문제에서는 꽉차있는 상태에서 하나씩 빼야한다.

def knapsack_mem(val, wt, mem, n, w):
    if n == 0 or w == 0:
        mem[n][w] = sum(val)
    if mem[n][w] == None:
        if wt[n - 1] > w:
            mem[n][w] = knapsack_mem(val, wt, mem, n - 1, w)
        else:
            valWith = knapsack_mem(val, wt, mem, n - 1, w - wt[n - 1]) - val[n - 1]
            valWithout = knapsack_mem(val, wt, mem, n - 1, w)
            mem[n][w] = min(valWith, valWithout)

    return mem[n][w]

print(knapsack_mem(val, wt, mem, n, W))

for i in mem:
    print(i)