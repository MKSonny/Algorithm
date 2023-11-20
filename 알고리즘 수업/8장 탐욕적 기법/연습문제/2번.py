coins = [25, 10, 5, 1]
V = 68

def min_coins_greedy(V, coins):
    cnt = []
    for i in range(len(coins)):
        j = V // coins[i]
        cnt.append(j)
        V -= coins[i] * j
    return cnt

print(min_coins_greedy(V, coins))