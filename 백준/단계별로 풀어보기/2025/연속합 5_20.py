import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

maxx = sum(l)
total = 0
rt = 0

while rt < len(l):
    total += l[rt]
    maxx = max(total, maxx)

    if total < 0:
        total = 0
    rt += 1

print(maxx)