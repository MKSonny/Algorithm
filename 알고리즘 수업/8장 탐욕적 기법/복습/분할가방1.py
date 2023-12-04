obj = [('A', 10, 80), ('B', 12, 120), ('C', 8, 60)]
obj.sort(key=lambda o:o[2]/o[1], reverse=True)
W = 18

def knapsack(obj, W):
    profit = 0
    for o in obj:
        if W - o[1] >= 0:
            profit += o[2]
            W -= o[1]
        else:
            wp = W / o[1]
            profit += wp * o[2]
            W = int(W - (o[1] * wp))
    print(profit)

knapsack(obj, W)