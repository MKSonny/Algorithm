import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l2 = list(map(int, sys.stdin.readline().split()))

l = set(l)
l2 = set(l2)

print(len((l - l2) | (l2 - l)))