def printNode(knapsack, level, weight, profit, bound, maxProfit):
    print("%d %-16s : %3.1fkg 가치/한계합 = %5.1f / %5.1f > %5.1f(최고합)"
          %(level, knapsack, weight, profit, bound, maxProfit))
# memo

def calculate_bound(obj, W, level, weight, profit):
    if weight > W:
        return 0
    pBound = profit
    for j in range(level + 1, len(obj)):
        pBound += obj[j][1]

    return pBound


def knapsack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound):
    printNode(knapsack, level, weight, profit, bound, maxProfit)

    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = calculate_bound(obj, W, level, newWeight, newProfit)
        if newBound >= maxProfit:
            knapsack.append(obj[level][2])
            maxProfit = knapsack_bnb(obj, knapsack, W, level + 1, newWeight, newProfit, maxProfit, newBound)
            knapsack.pop()

    newWeight = weight
    newProfit = profit
    newBound = calculate_bound(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit:
        maxProfit = knapsack_bnb(obj, knapsack, W, level + 1, newWeight, newProfit, maxProfit, newBound)

    return maxProfit


obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10
knapsack_bnb(obj, [], 10, 0, 0, 0, 0, 0)