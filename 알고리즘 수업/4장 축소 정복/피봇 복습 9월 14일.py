def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]

    while low <= high:
        while A[low] <= pivot: low += 1
        while A[high] > pivot: high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]

list = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(list)
partition(list, 0, len(list) - 1)
print(list)