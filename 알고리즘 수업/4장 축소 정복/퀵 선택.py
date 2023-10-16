def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right
    while low <= high:
        while low <= right and a[low] <= pivot: low += 1
        while high >= left and a[high] > pivot: high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

    a[left], a[high] = a[high], a[left]

    return high

def quick_select(a, left, right, k):
    pos = partition(a, left, right)
    if pos + 1 == left + k:
        return a[pos]
    elif pos + 1 < left + k:
        return quick_select(a, pos + 1, right, left - (pos + 1) + k)
    else:
        return quick_select(a, left, pos - 1, k)

def quick_select_rev(a, left, right, k):
    pos = partition(a, left, right)
    rank = right - pos + 1  # 현재 위치의 요소는 오른쪽 부분의 rank번째로 큰 요소입니다.
    if rank == k:
        return a[pos]
    elif rank < k:
        return quick_select_rev(a, left, pos - 1, k - rank)
    else:
        return quick_select_rev(a, pos + 1, right, k)




data = [1, 2, 3, 4, 5]
print(quick_select(data, 0, len(data) - 1, 1))
print(quick_select_rev(data, 0, len(data) - 1, 1))