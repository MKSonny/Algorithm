def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    lt = left
    rt = mid + 1
    n = len(A)
    k = left
    temp = [0] * n
    while lt <= mid and rt <= right:
        if A[lt] <= A[rt]:
            temp[k] = A[lt]
            lt += 1
            k += 1
        else:
            temp[k] = A[rt]
            rt += 1
            k += 1
    if lt > mid:
        temp[k: k + right - rt + 1] = A[rt: right + 1]
    else:
        temp[k: k + mid - lt + 1] = A[lt: mid + 1]
    A[left: right + 1] = temp[left: right + 1]

list = [4, 3, 2, 8, 9, 1]
print(list)
merge_sort(list, 0, len(list) - 1)
print(list)