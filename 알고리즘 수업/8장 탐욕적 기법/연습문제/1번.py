# 866원에 대해 탐욕적 기법의 min_coins_greedy0(알고리즘 8.1)가 수행되는 과정을 설명하라.
coins = [500, 100, 50, 10, 5, 1]
V = 866

def min_coins_greedy(V, coins):
    cnt = []
    for i in range(len(coins)):
        j = V // coins[i]
        cnt.append(j)
        V -= coins[i] * j
    return cnt

print(min_coins_greedy(V, coins))