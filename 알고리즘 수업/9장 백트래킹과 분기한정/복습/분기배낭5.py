obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def calc_bound(W, obj, level, profit, weight):
    if weight > W:
        return 0

    pBound = profit
    for i in range(level + 1, len(obj)):
        pBound += obj[i][1]

    return pBound

def knapsack_bnb(knapsack, bound, obj, W, weight, level, profit, maxProfit):
    print("%d %-16s : 가치/한계합 %3.1f / %3.1f 최대 가치: %3.1f" % (level, knapsack, profit, bound, maxProfit))
    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = calc_bound(W, obj, level, newProfit, newWeight)

        if newBound >= maxProfit:
            knapsack.append(obj[level][2])
            maxProfit = knapsack_bnb(knapsack, newBound, obj, W, newWeight, level + 1, newProfit, maxProfit)
            knapsack.pop()

    newWeight = weight
    newProfit = profit

    newBound = calc_bound(W, obj, level, newProfit, newWeight)

    if newBound >= maxProfit:
        maxProfit = knapsack_bnb(knapsack, newBound, obj, W, newWeight, level + 1, newProfit, maxProfit)

    return maxProfit

print(knapsack_bnb([],0,obj, W, 0, 0, 0, 0))