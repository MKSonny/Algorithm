import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))

    money = 0
    maxPrice = 0

    for i in range(len(price) - 1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else:
            money += maxPrice - price[i]

    print(money)