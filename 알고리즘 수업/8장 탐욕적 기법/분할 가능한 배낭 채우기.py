def knapsack_fractional_greedy(obj, W):
    obj.sort(key = lambda o: o[2]/o[1], reverse = True)

    totalValue = 0
    for o in obj:
        if W <= 0:
            break
        if W - o[1] >= 0:
            W -= o[1]
            totalValue += o[2]
        else:
            fraction = W / o[1]
            totalValue += o[2] * fraction
            W = int(W - (o[1] * fraction))

    return totalValue

obj = [('A', 10, 80), ('B', 12, 120), ('C', 8, 60)]
obj.sort(key=lambda o: o[2] / o[1], reverse=True)
print(obj)
print("W = 18 ", obj)
print("부분적인 배낭(18): ", knapsack_fractional_greedy(obj, 18), end="\n\n")

obj = [('A', 10, 60), ('B', 40, 40), ('C', 20, 100), ('D', 30, 120)]
print("W = 50 ", obj)
print("부분적인 배낭(50): ", knapsack_fractional_greedy(obj, 50))