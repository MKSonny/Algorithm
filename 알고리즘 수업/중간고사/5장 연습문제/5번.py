def str_merge(string, left, mid, right):
    i = left
    j = mid + 1
    k = left
    sorted = ['x'] * len(string)

    while i <= mid and j <= right:
        if string[i] <= string[j]:
            sorted[k] = string[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = string[j]
            j, k  = j + 1, k + 1

    if i > mid:
        sorted[k: k + right - j + 1] = string[j: right + 1]
    else:
        sorted[k: k + mid - i + 1] = string[i: mid + 1]

    string[left: right + 1] = sorted[left: right + 1]


def str_merge_sort(string, left, right):
    if left < right:
        mid = (left + right) // 2
        str_merge_sort(string, left, mid)
        str_merge_sort(string, mid + 1, right)
        str_merge(string, left, mid, right)

str_ = list('ALGORITHM')
str_merge_sort(str_, 0, len(str_) - 1)
print(str_)