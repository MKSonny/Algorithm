import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

maxx = -1
cnt = 1
for i in range(n - m + 1):
    a = sum(l[i:i + m])
    if maxx == a:
        cnt += 1
    maxx = max(maxx, a)

if maxx == 0:
    print("SAD")
else:
    print(maxx)
    print(cnt)