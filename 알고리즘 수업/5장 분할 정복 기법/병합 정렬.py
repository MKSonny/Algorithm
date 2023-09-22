def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    lt = left
    k = left
    sorted = [0] * len(A)
    rt = mid + 1
    while lt <= mid and rt <= right:
        if A[lt] < A[rt]:
            sorted[k] = A[lt]
            k, lt = k + 1, lt + 1
        else:
            sorted[k] = A[rt]
            k, rt = k + 1, rt + 1
    if lt > mid:
        sorted[k : k + right - rt + 1] = A[rt: right + 1]
    else:
        sorted[k : k + mid - rt + 1] = A[lt: mid + 1]
    A[left: right + 1] = sorted[left: right + 1]

list = [1, 3, 7, 8, 2, 4, 5, 9]
print(list)
merge_sort(list, 0, len(list) - 1)
print(list)