obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10

def calc_bound(W, weight, profit, obj, level):
    if weight > W:
        return 0

    pBound = profit

    for i in range(level + 1, len(obj)):
        pBound += obj[i][1]

    return pBound

# 1 ['A']            : 2.5kg 가치/한계합 =  30.0 / 250.0 >  30.0(최고합)
def printKnapsack(level, knapsack, weight, profit, bound, maxProfit):
    print("%d %-16s : %3.1f 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)" % (level, knapsack, weight, profit, bound, maxProfit))

def knapsack_bnb(knapsack, obj, W, weight, profit, level, maxProfit, bound):
    printKnapsack(level, knapsack, weight, profit, bound, maxProfit)

    if level == len(obj):
        return maxProfit

    if obj[level][0] + weight <= W:
        newWeight = obj[level][0] + weight
        newProfit = obj[level][1] + profit

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = calc_bound(W, newWeight, newProfit, obj, level)

        if newBound >= maxProfit:
            knapsack.append(obj[level][2])
            maxProfit = knapsack_bnb(knapsack, obj, W, newWeight, newProfit, level + 1, maxProfit, newBound)
            knapsack.pop()

    newWeight = weight
    newProfit = profit

    newBound = calc_bound(W, newWeight, newProfit, obj, level)

    if newBound >= maxProfit:
        maxProfit = knapsack_bnb(knapsack, obj, W, newWeight, newProfit, level + 1, maxProfit, newBound)

    return maxProfit



print(knapsack_bnb([], obj, W, 0, 0, 0, 0, 0))