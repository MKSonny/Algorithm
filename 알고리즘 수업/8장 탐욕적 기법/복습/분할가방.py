obj = [('A', 10, 80), ('B', 12, 120), ('C', 8, 60)]
W = 18
def knapsack(obj, W):
    obj.sort(key = lambda o : o[2] / o[1], reverse = True)
    profit = 0

    for o in obj:
        if W - o[1] >= 0:
            profit += o[2]
            W -= o[1]
        else:
            fraction = W / o[1]
            profit += o[2] * fraction
            W = int(W - (o[1] * fraction))

    return profit

print(knapsack(obj, W))