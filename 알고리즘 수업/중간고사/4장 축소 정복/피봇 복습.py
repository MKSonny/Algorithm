list = [5, 3, 8, 4, 9, 1, 6, 2, 7]

def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if pos + 1 == left + k:
        return A[pos]
    elif pos + 1 > left + k:
        quick_select(A, left, pos - 1, k)
    else:
        quick_select(A, pos + 1, right, k - (pos + 1 + left))

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]

    while low <= high:
        while A[low] <= pivot and low <= right: low += 1
        while A[high] >= pivot and high >= left: high -= 1

        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]

    return high

print(partition(list, 0, len(list) - 1))
