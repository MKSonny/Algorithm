obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(obj, W, weight, profit, level):
    if weight > W:
        return

    pBound = profit

    for j in range(level + 1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapsack(obj, W, weight, profit, level, maxProfit):
    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(obj, W, weight, profit, level)

        if newBound >= maxProfit:
            maxProfit = knapsack(obj, W, newWeight, newProfit, level + 1, maxProfit)

    newWeight = weight
    newProfit = profit

    newBound = bound(obj, W, weight, profit, level)
    if newBound >+ maxProfit:
        maxProfit = knapsack(obj, W, newWeight, newProfit, level + 1, maxProfit)

    return maxProfit

print(knapsack(obj, W, 0, 0, 0, 0))