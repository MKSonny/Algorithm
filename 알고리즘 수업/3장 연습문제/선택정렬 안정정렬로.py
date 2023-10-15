def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[j] == a[i]:
                a[i], a[j] = a[j], a[i]
            