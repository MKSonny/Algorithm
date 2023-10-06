def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[least], a[i] = a[i], a[least]


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(data)
selection_sort(data)
print(data)