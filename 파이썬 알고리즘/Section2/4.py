n = 10
a = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]

avg = int(sum(a)/n + 0.5)
res = 0
min = 99999

for idx, x in enumerate(a):

    temp = abs(avg - a[idx])

    if min > temp:
        print('temp', temp)
        min = temp
        score = x
        res = idx + 1
    elif min == temp:
        if x > score:
            score = x
            res = idx + 1
print(res)