def merge(a, left, mid, right):
    k = left
    i = left
    j = mid + 1
    d = [0] * len(a)
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            d[k] = a[i]
            i += 1
            k += 1
        else:
            d[k] = a[j]
            j += 1
            k += 1

    if i > mid:
        d[k: k + right - j + 1] = a[j: right + 1]
    else:
        d[k: k + mid - i + 1] = a[i: mid + 1]

    a[left: right + 1] = d[left: right + 1]


def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)


data = [1, 3, 7, 8, 2, 4, 5, 9]
print(data)
merge_sort(data, 0, len(data) - 1)
print(data)
