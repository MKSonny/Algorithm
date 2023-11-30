obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(W, weight, level, obj, profit):
    if weight > W:
        return 0

    pbound = profit

    for i in range(level + 1, len(obj)):
        pbound += obj[i][1]

    return pbound

def knapsack(W, obj, level, weight, profit, maxProfit):
    if level == len(obj):
        return maxProfit

    if obj[level][0] + weight <= W:
        newProfit = obj[level][1] + profit
        newWeight = obj[level][0] + weight

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(W, newWeight, level, obj, newProfit)

        if newBound >= maxProfit:
            maxProfit = knapsack(W, obj, level + 1, newWeight, newProfit, maxProfit)

    newProfit = profit
    newWeight = weight

    newBound = bound(W, newWeight, level, obj, newProfit)
    if newBound >= maxProfit:
        maxProfit = knapsack(W, obj, level + 1, newWeight, newProfit, maxProfit)

    return maxProfit

print(knapsack(W, obj, 0, 0, 0, 0))