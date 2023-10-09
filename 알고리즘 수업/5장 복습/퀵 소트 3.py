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
        a[high], a[left] = a[left], a[high]
    return high

def quick_sort(a, left, right):
    if left < right:
        pos = partition(a, left, right)
        quick_sort(a, left, pos - 1)
        quick_sort(a, pos + 1, right)

data = [4, 5, 1, 9, 7, 6]
quick_sort(data, 0, len(data) - 1)
print(data)