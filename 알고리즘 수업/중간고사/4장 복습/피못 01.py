list = [5, 3, 8, 4, 9, 1, 6, 2, 7]

def quick_select(A, left, right, k):
    idx = partition(A, left, right)
    if idx + 1 == left + k:
        return A[idx]
    if idx + 1 > left + k:
        return quick_select(A, left, idx - 1, k)
    else:
        return quick_select(A, idx + 1, right, k - (idx + 1 - left))

def partition(data, left, right):
    pivot = data[left]
    low = left + 1
    mid = (left + right) // 2
    high = right

    while low <= mid and high >= mid + 1:
        while data[low] <= pivot: low += 1
        while data[high] > pivot: high -= 1
        if low < high:
            data[low], data[high] = data[high], data[low]

    if low > high:
        data[low], data[high] = data[high], data[low]

    return high

print(list)
num = quick_select(list, 0, len(list) - 1, 6)
print(list)
print(num)