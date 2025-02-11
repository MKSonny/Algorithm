import sys

n, m = map(int, sys.stdin.readline().split())

lo = []
sc = []

for _ in range(n):
    lo.append(sys.stdin.readline().rstrip().split())

for _ in range(m):
    sc.append(int(sys.stdin.readline()))

def find(num):
    l, r = 0, n

    while l <= r:
        mid = (l + r) // 2
        if num > int(lo[mid][1]):
            l = mid + 1
            # return mid
        else:
            r = mid - 1
    print(lo[l][0])

for i in sc:
    find(i)