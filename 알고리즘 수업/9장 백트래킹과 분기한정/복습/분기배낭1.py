obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10
# 5 ['B', 'C', 'D']  : 9.9kg 가치/한계합 = 180.0 / 180.0 > 180.0(최고합)
def print_knapsack(level, knapsack, weight, profit, bound, maxProfit):
    print("%d %-16s : %3.1f 가치/한계합 = %3.1f / %3.1f > %3.1f(최고합)" % (level, knapsack, weight, profit, bound, maxProfit))


def calc_bound(W, level, obj, weight, profit):
    if weight > W:
        return 0

    pBound = profit

    for i in range(level + 1, len(obj)):
        pBound += obj[i][1]

    return pBound

def knapsack_bnb(W, level, knapsack, bound, obj, profit, weight, maxProfit):
    print_knapsack(level, knapsack, weight, profit, bound, maxProfit)

    if level == len(obj):
        return maxProfit

    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]

        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = calc_bound(W, level, obj, newWeight, newProfit)

        if newBound >= maxProfit:
            knapsack.append(obj[level][2])
            maxProfit = knapsack_bnb(W, level + 1, knapsack, newBound, obj, newProfit, newWeight, maxProfit)
            knapsack.pop()

    newWeight = weight
    newProfit = profit

    newBound = calc_bound(W, level, obj, newWeight, newProfit)

    if newBound >= maxProfit:
        maxProfit = knapsack_bnb(W, level + 1, knapsack, newBound, obj, newProfit, newWeight, maxProfit)

    return maxProfit

print(knapsack_bnb(W, 0, [], 0, obj, 0, 0, 0))