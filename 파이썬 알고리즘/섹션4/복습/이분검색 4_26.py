'''
8 32
23 87 65 12 57 32 99 81
'''
a, b = input().split()
l = list(map(int, input().split()))
l.sort()
# print(l)

def find(l, key, first, last):
    mid = (first + last) // 2
    if l[mid] == key:
        return mid + 1

    if l[mid] < key:
        first = mid + 1
        return find(l, key, first, last)
    else:
        last = mid - 1
        return find(l, key, first, last)


# 0, 8 -> 4
m = find(l, int(b), 0, len(l) - 1)
print(m)