def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right
    while low <= high:
        while low <= right and a[low] <= pivot: low += 1
        while high >= left and a[high] > pivot: high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]
    if low > high:
        a[left], a[high] = a[high], a[left]
    return high

def quick_sort(a, left, right):
    if left < right:
        pos = partition(a, left, right)
        # 왜 피봇은 정렬하지 않는가?
        quick_sort(a, left, pos - 1)
        quick_sort(a, pos + 1, right)

data = [3, 2, 6, 9, 1, 5]
print(data)
quick_sort(data, 0, len(data) - 1)
print(data)