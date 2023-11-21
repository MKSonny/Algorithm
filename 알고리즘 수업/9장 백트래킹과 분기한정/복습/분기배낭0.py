obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def bound(obj, W, weight, level, profit):
    if weight > W:
        return

    pBound = profit

    for j in range(level + 1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapsack(obj, W, weight, level, profit):
    maxProfit = profit
    if level == len(obj):
        return maxProfit

    if obj[level][]