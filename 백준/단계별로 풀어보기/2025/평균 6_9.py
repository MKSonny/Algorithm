import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

m = max(l)

total = 0

for i in l:
    total += (i / m) * 100

print(total / n)