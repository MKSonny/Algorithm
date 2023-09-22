def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid - 1)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

sorted = []

def merge(A, left, mid, right):
    # left = 0, right = 3
    low = left
    high = mid + 1
    k = left
    while low <= mid and high <= right:
        if A[low] <= A[high]:
            sorted[k] = A[low]
            low += 1
            k += 1
        else:
            sorted[k] = A[high]
            high += 1
            k += 1

    if low > mid:
        sorted[k: right + 1] = A[j: right + 1]
    else:
        sorted[k: ]

list = [1, 3, 7, 8, 2, 4, 5, 9]
print(list)
merge_sort(list, 0, len(list) - 1)
print(list)