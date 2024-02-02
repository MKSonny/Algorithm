import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0

summ = sum(l[:m])
maxx = summ

for i in range(n - m):
    summ = summ - l[i] + l[i + m]
    maxx = max(summ, maxx)

print(maxx)