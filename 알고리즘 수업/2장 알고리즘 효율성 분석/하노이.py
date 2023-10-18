def partition(a, left, right):
    low = left + 1
    pivot = a[left]
    high = right

    while low <= high:
        while low <= right and a[low] <= pivot:
            low += 1
        while high >= left and a[high] > pivot:
            high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

    a[high], a[left] = a[left], a[high]
    return high

def merge(a, left, mid, right):
    i = left
    k = left
    j = mid + 1
    tmp = [0] * len(a)

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1

    if i > mid:
        tmp[k : k + right - j + 1] = a[j : right + 1]
    else:
        tmp[k : k + mid - i + 1] = a[i : mid + 1]
    a[left : right + 1] = tmp[left : right + 1]


def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)

def quick_sort(a, left, right):
    if left < right:
        pos = partition(a, left, right)
        quick_sort(a, left, pos - 1)
        quick_sort(a, pos + 1, right)


data = [4, 2, 1, 9, 10, 3]
merge_sort(data, 0, len(data) - 1)
# quick_sort(data, 0, len(data) - 1)
print(data)