def bound(obj, W, level, weight, profit):
    if weight > W:
        return 0

    pBound = profit
    for j in range(level + 1, len(obj)):
        pBound += obj[j][1]

    return pBound

def knapSack_bnb(obj, W, level, weight, profit, maxProfit):
    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit:
            maxProfit = knapSack_bnb(obj, W, level + 1, newWeight, newProfit, maxProfit)


    newWeight = weight
    newProfit = profit
    newBound = bound(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit:
        maxProfit = knapSack_bnb(obj, W, level + 1, newWeight, newProfit, maxProfit)


    return maxProfit

obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
print(obj)
print("0-1 배낭문제(분기 한정):", knapSack_bnb(obj, 10, 0, 0, 0, 0))