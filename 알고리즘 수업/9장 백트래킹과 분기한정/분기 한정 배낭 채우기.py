'''
bound 함수: 현재 상태에서 가능한 최대 이익을 계산하는 함수로,
현재 무게에서 배낭에 넣을 수 있는 물건들의 가치를 더합니다.
이 함수는 상한치를 계산하는 역할을 합니다.
'''
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

    # 물건을 담는다.
    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        if newProfit > maxProfit:
            maxProfit = newProfit

        newBound = bound(obj, W, level, newWeight, newProfit)
        # newBound: 한계합
        if newBound >= maxProfit:
            maxProfit = knapSack_bnb(obj, W, level + 1, newWeight, newProfit, maxProfit)

    # 만약 가방의 용량을 넘으면 물건을 뺀다.
    # = 이전의 weight와 profit을 유지한다.
    # 하지만 level은 증가되서 함수를 들어왔으므로
    # 여기서 bound 함수가 실행 될 때 현재 물건을 제외한
    # 한계합을 계산한다.
    newWeight = weight
    newProfit = profit
    newBound = bound(obj, W, level, newWeight, newProfit)
    if newBound >= maxProfit:
        maxProfit = knapSack_bnb(obj, W, level + 1, newWeight, newProfit, maxProfit)


    return maxProfit

obj = [(2.5, 30, 'A'), (3.2, 50, 'B'), (1.7, 70, 'C'), (5, 60, 'D'), (4.1, 40, 'E'), ]
W = 10
print(obj)
print("0-1 배낭문제(분기 한정):", knapSack_bnb(obj, W, 0, 0, 0, 0))