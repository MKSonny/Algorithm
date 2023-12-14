coins = [500, 100, 50, 10, 5, 1]
V = 580

def calc(coins, V):
    c = []
    for i in range(len(coins)):
        cnt = V // coins[i]
        c.append(cnt)
        V -= cnt * coins[i]
    print(c)

calc(coins, V)