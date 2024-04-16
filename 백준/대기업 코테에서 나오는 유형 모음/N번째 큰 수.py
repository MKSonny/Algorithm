import sys

n = int(sys.stdin.readline())
l = []
temp = []

for i in range(1, n + 1):
    if n * i > n * n - n - n:
        l += list(map(int, sys.stdin.readline().rstrip().split()))
    else:
        sys.stdin.readline()
        continue

l.sort(reverse=True)
# print(l)
# 20(n * n - n)개를 넘겨야
# print(l)
print(l[n - 1])