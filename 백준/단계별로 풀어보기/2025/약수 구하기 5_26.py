import sys

n, m = map(int, sys.stdin.readline().split())

l = []

for i in range(1, n + 1):
    if n % i == 0:
        l.append(i)

if m > len(l):
    print(0)
else:
    print(l[m - 1])