import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

h = {}

for v in l:
    h[v] = 1

# print(h)

for v in k:
    if v in h:
        print(1, end=' ')
    else:
        print(0, end=' ')