def count_inversion(a):
    n = len(a)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inv_count += 1

    return inv_count

def merge_sort(a, tmp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(a, tmp, left, mid)
        inv_count += merge_sort(a, tmp, mid + 1, right)
        inv_count += merge(a, tmp, left, mid, right)

    return inv_count

def merge(a, tmp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    if i <= mid:
        tmp[k : k + mid - i + 1] = a[i : mid + 1]
    else:
        tmp[k : k + right - j + 1] = a[j : right + 1]

    a[left : right + 1] = tmp[left : right + 1]
    return inv_count

data = [1, 5, 2, 3, 8, 10]

def count_inversion_dc(arr):
    n = len(arr)
    tmp = [0] * n
    return merge_sort(arr, tmp, 0, n - 1)

print(count_inversion_dc(data))