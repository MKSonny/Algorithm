import sys

n = sys.stdin.readline()
l = list(map(int, sys.stdin.readline().split()))

l.sort()
print(l[-1] * l[0])