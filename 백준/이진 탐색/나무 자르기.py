import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

# print(l)
# result_list = [x - 5 for x in l]
# print(result_list)
# print(l)

def binary_search(l, lt, rt, key):
    if lt > rt:
        return rt
    mid = (lt + rt) // 2
    ssum = 0
    for v in l:
        if v - mid < 0:
            continue
        ssum += v - mid
    if ssum == key:
        # mid += 1
        return mid
    elif ssum > key:
        return binary_search(l, mid + 1, rt, key)
    else:
        return binary_search(l, lt, mid - 1, key)

print(binary_search(l, 0, max(l), m))