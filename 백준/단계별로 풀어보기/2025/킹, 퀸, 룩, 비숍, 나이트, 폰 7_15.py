import sys

l = list(map(int, sys.stdin.readline().split()))

# 1, 1, 2, 2, 2, 8
a = [1, 1, 2, 2, 2, 8]

for i in range(len(l)):
    print(a[i] - l[i], end=' ')