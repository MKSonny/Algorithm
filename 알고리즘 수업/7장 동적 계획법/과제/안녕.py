wt = [1, 21, 79]
val = [20, 30, 25]
W = 100
n = len(val)

def knapsack(val, wt, W, n):
    table = [[0 for _ in range(W)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W):
            if wt[i - 1] > w:
                table[i][w] = table[i - 1][w]
            else:
                valWith = val[i - 1] + table[i - 1][w - wt[i - 1]]
                valWithout = table[i - 1][w]
                table[i][w] = max(valWith, valWithout)

    return table[n][W - 1]

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

# print('hp', hp)
# print('happy', happy)

print(knapsack(happy, hp, W, n))