def merge(a, left, mid, right, tmp):
    i = left
    j = mid + 1
    k = left
    cnt = 0
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            cnt += mid - i + 1
            j += 1
        k += 1
    if i > mid:
        tmp[k : k + right - j + 1] = a[j : right + 1]
    else:
        tmp[k : k + mid - i + 1] = a[i : mid + 1]

    a[left : right + 1] = tmp[left:right + 1]
    return cnt

def merge_sort(a, left, right, tmp):
    cnt = 0
    if left < right:
        mid = (left + right) // 2
        cnt += merge_sort(a, left, mid, tmp)
        cnt += merge_sort(a, mid + 1, right, tmp)
        cnt += merge(a, left, mid, right, tmp)
    return cnt

def count_reverse(a):
    tmp = [0] * len(a)
    return merge_sort(a, 0, len(data) - 1, tmp)

data = [1, 5, 2, 3, 8, 10]
print(count_reverse(data))