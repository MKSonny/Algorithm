n, m = map(int, input().split())

l = list(map(int, input().split()))

'''
15 99
73 32 31 49 94 37 40 62 78 66 27 100 99 29 9 
'''

l.sort()

print(l)

def binary_search(l, lt, rt, key):
    while lt <= rt:
        mid = (lt + rt) // 2
        if l[mid] == key:
            return mid + 1
        elif l[mid] < key:
            lt = mid + 1
        else:
            rt = mid - 1

print(binary_search(l, 0, n - 1, m))