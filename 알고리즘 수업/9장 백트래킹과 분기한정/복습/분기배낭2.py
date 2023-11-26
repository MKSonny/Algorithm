obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(W, weight, obj, profit, level):
    if weight > W:
        return 0

    pbound = profit

    for i in range(level + 1, len(obj)):
        pbound += obj[i][1]

    return pbound

def dfs_knapsack(W, obj, level, weight, profit, maxprofit):
    if obj[level][0] + weight <= W:
        newProfit = obj[level][1] + profit
        newWeight = obj[level][0] + weight

        if newProfit > maxprofit:
            maxprofit = newProfit

        newBound = bound(W, newWeight, obj, newProfit, level)

        if newBound > maxprofit:
            maxprofit = dfs_knapsack(W, obj, level + 1, newWeight, newProfit, maxprofit)

    newWeight = weight
    newProfit = profit

    newBound = bound(W, newWeight, obj, newProfit, level)
    if newBound > maxprofit:
        maxprofit = dfs_knapsack(W, obj, level + 1, newWeight, newProfit, maxprofit)

    return maxprofit

print(dfs_knapsack(W, obj, 0, 0, 0, 0))