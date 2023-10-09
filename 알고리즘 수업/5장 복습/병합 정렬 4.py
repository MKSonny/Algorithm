def merge(a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    sorted = [0] * len(a)
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = a[j]
            j, k = j + 1, k + 1
    if i > mid:
        sorted[k: k + right - j + 1] = a[j : right + 1]
    else:
        sorted[k: k + mid - i + 1] = a[i : mid + 1]

    a[left: right + 1] = sorted[left: right + 1]

def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)

data = [5, 2, 3, 9, 1, 4]
print(data)
merge_sort(data, 0, len(data) - 1)
print(data)