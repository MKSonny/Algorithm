obj = [('A', 10, 80), ('B', 12, 120), ('C', 8, 60)]
W = 18

def knapsack(obj, W):
    obj.sort(key = lambda o:o[2]/o[1], reverse = True)
    totalValue = 0
    for o in obj:
        if W <= 0:
            break
        if W - o[1] >= 0:
            totalValue += o[2]
            W -= o[1]
        else:
            fraction = W / o[1]
            totalValue += fraction * o[2]
            W = int(W - fraction * o[1])
    return totalValue

print(knapsack(obj, W))