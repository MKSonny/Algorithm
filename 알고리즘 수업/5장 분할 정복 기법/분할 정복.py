def merge_sort(A, left, right):
    # left = 0
    # right = 7
    if left < right:
        # mid = 3
        # 왼쪽 ~ 가운데 기준 분할
        mid = (left + right) // 2

        # 1) merge_sort(list, 0, 3)
        # 2) merge_sort(list, 0, 1)
        # 4) merge_sort(list, 2, 4)  left = 2, right = 7, mid = 4
        # 6) merge_sort(list, 5, 6) left = 5, right = 7, mid = 6
        merge_sort(A, left, mid)
        # 3) merge_sort(list, 2, 7)
        # 5) merge_sort(list, 5, 7)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    k = left
    i = left
    j = mid + 1
    sorted = [0] * (right - left + 1)
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]
            j, k = j + 1, k + 1

    if i > mid:
        sorted[k : k + right - j + 1] = A[j : right + 1]
    else:
        sorted[k : k + mid - i + 1] = A[i : mid + 1]

    A[left : right + 1] = sorted[left : right + 1]

list = [8, 1, 7, 3, 9, 2, 4, 5]
test_list = [1, 8, 3, 7]

print(list)
merge(list, 0, 6, 7)
print(list)
merge(list, 0, 4, 7)
print(list)
merge(list, 0, 2, 7)
print(list)
merge(list, 0, 1, 7)
print(list)
merge(list, 0, 3, 7)
print(list)