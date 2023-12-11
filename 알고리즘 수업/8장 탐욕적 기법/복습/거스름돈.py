coins = [500, 100, 50, 10, 5, 1]
V = 580

def calc_coins(coins, V):
    count = []
    for i in range(len(coins)):
        cnt = V // coins[i]
        count.append(cnt)
        V -= coins[i] * cnt
    return count

print(calc_coins(coins, V))