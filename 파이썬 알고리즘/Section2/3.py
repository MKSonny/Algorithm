a = 4
b = 6
list = [0] * (a + b + 1)

def find_max_sum(a, b):
    max = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            list[i + j] += 1
    for k in range(a + b + 1):
        if max <= list[k]:
            max = list[k]
    for i in range(a + b):
        if list[i] == max:
            print(i, end=' ')
find_max_sum(4, 6)