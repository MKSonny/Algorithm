def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] >= key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
data = [9, 8, 7, 5, 6, 5]
print(data)
insertion_sort(data)
print(data)