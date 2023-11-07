obj = [('A', 10, 80), ('B', 12, 120), ('C', 8, 60)]
W = 18
# 6
def knap(obj, W):
    obj.sort(key = lambda o: o[2]/o[1], reverse = True)
    print(obj)
    total = 0
    for i in range(len(obj)):
        if obj[i][1] < W:
            W -= obj[i][1]
            total += obj[i][2]
        else:
            total += W * (obj[i][2] / obj[i][1])
            break

    return total

print(knap(obj, W))