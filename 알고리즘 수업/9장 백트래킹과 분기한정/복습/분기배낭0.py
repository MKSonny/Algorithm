obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(obj, W, weight, level, profit):
    if weight > W:
        return

    pBound = profit

    for j in range(level + 1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapsack(obj, W, weight, level, profit, maxProfit):
    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newProfit = profit + obj[level][1]
        newWeight = profit + obj[level][0]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(obj, W, newWeight, level, newProfit)

        if newBound >= maxProfit:
            knapsack(obj, W, newWeight, level + 1, newProfit, maxProfit)
