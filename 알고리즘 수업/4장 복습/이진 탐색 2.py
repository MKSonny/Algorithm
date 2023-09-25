data = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41, 44, 49]

def binary_search(data, left, right, find):
    mid = (left + right) // 2
    if data[mid] == find:
        return mid
    if data[mid] < find:
        return binary_search(data, mid + 1, right, find)
    else:
        return binary_search(data, left, mid - 1, find)

idx = binary_search(data, 0, len(data) - 1, 30)
print(idx)