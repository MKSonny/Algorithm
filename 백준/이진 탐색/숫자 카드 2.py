import copy
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

answer = copy.deepcopy(k)
counts = {}

for num in answer:
    counts[num] = 0

# print(counts)

k.sort()
# print(l)
# print(k)

def binary_search(k, key):
    lt = 0
    rt = len(k) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if k[mid] == key:
            return True
        elif k[mid] < key:
            lt = mid + 1
        else:
            rt = mid - 1
    return False

a = []

for value in l:
    if binary_search(k, value):
        counts[value] += 1

for value in counts.values():
    print(value, end=' ')