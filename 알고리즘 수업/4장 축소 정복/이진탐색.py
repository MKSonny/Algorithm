list = [1, 3, 8, 13, 13, 16, 21, 26, 27, 30, 33, 36, 39, 41, 44, 49]

def binary_search_recursive(list, first, last, key):

    if (last >= first):
        mid = (first + last) // 2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            return binary_search_recursive(list, first, mid - 1, key)
        else:
            return binary_search_recursive(list, mid + 1, last, key)

def binary_search(list, last, key):
    first = 0
    while (last >= first):
        mid = (last + first) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            first = mid + 1
        else:
            last = mid - 1

index = binary_search_recursive(list, 0, len(list), 33)

print(index)