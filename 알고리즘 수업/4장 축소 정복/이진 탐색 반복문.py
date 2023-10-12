def binary_search(a, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid]:
            return mid
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

data = [1, 2, 3, 4, 5]
idx = binary_search(data, 5, 0, len(data) - 1)
print(idx)