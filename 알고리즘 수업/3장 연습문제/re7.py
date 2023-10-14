def find(a, k):
    n = len(a)
    a.append(k)
    i = 0
    while a[i] != k:
        i += 1
    if i == n:
        return -1
    return i

data = [1, 2, 3, 4, 5]
print(find(data, 5))