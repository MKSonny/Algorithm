'''
8 32
23 87 65 12 57 32 99 81
'''

n, m = map(int, input().split())

l = list(map(int, input().split()))
l.sort()

def binary_find(l, key, low, high):
    while low <= high:
        mid = (low + high) // 2

        if key == l[mid]:
            return (mid + 1)
        elif key < l[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(binary_find(l, m, 0, len(l)))