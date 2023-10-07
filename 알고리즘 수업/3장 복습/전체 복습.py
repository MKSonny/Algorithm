def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[i], a[least] = a[least], a[i]


data = [4, 2, 1, 6, 7, 3]
print(data)
selection_sort(data)
print(data)