import copy
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

h = {}

for value in l:
    if value in h:
        h[value] += 1
    else:
        h[value] = 1

for value in k:
    if value in h:
        print(h[value], end=' ')
    else:
        print(0, end=' ')