def partition(A, left, right):
    low = left + 1
    high = right + 1
    pivot = A[left]

    while low <= high:
        while low <= right and low <= pivot: low += 1
        while high >= left and high >= pivot: high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]

        A[left], A[high] = A[high], A[left]

        return high

def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if pos + 1 == left + k:
        return A[pos]
    elif pos + 1 < left + k:
        

list = [5, 3, 8, 4, 9, 1, 6, 2, 7]

print(partition(list, 0, len(list)))