data = [5, 3, 8, 4, 9, 2, 7]

def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right
    while low <= high:
        while low <= right and a[low] <= pivot:
            low += 1
        while a[high] > pivot and high >= left:
            high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]
    a[high], a[left] = a[left], a[high]
    return high

def quick_sort(a, left, right):
    if left < right:
        mid = partition(a, left, right)
        quick_sort(a, left, mid - 1)
        quick_sort(a, mid + 1, right)

def binary_search(a, left, right, key):
    if left < right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            return binary_search(a, left, mid, key)
        else:
            return binary_search(a, mid + 1, right, key)


print(data)
quick_sort(data, 0, len(data) - 1)
idx = binary_search(data, 0, len(data) - 1, 5)
print(data)
print(idx)