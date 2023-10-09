def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def insertion_sort_recursive(a, n):
    if n <= 1:
        return

    insertion_sort_recursive(a, n - 1)

    key = a[n - 1]
    j = n - 2

    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key


data = [5, 3, 8, 4, 9, 1, 2, 7]
print(data)
insertion_sort_recursive(data, len(data))
print(data)