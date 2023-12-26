import sys

input = sys.stdin.readline

def binary_search_iter(A, key, low, high):
    while low <= high:
        # low = 0, high = 1
        mid = (low + high) // 2
        # mid = 0
        if key == A[mid]:
            return 1
        elif key > A[mid]:
            low = mid + 1
        else:
            # high = 1
            high = mid - 1
    return 0

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
find = list(map(int, input().split()))

for find_num in find:
    print(binary_search_iter(A, find_num, 0, n - 1))