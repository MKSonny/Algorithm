import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

total = 0

prev = h[0]
for i in range(n - 1):
    if prev > h[i]:
        prev = h[i]
    total += prev * l[i]

print(total)