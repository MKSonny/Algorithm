obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(obj, weight, W, level, profit):
    if weight > W:
        return 0

    pbound = profit

    for i in range(level + 1, len(obj)):
        pbound += obj[i][1]

    return pbound

def knapsack(W, obj, level, weight, profit, maxprofit):
    if level == len(obj):
        return maxprofit

    if weight + obj[level][0] <= W:
        newProfit = profit + obj[level][1]
        newWeight = weight + obj[level][0]

        if newProfit > maxprofit:
            maxprofit = newProfit

        newBound = bound(obj, newWeight, W, level, newProfit)

        if newBound >= maxprofit:
            maxprofit = knapsack(W, obj, level + 1, newWeight, newProfit, maxprofit)

    newWeight = weight
    newProfit = profit

    newBound = bound(obj, newWeight, W, level, newProfit)

    if newBound >= maxprofit:
        maxprofit = knapsack(W, obj, level + 1, newWeight, newProfit, maxprofit)

    return maxprofit

print(knapsack(W, obj, 0, 0, 0, 0))