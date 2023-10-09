def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

data = [3, 5, 8, 4, 9, 1, 6, 2, 7]
print(data)
insertion_sort(data)
print(data)