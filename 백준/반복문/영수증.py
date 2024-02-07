import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
l = []
for _ in range(m):
    l.append(map(int, sys.stdin.readline().split()))
total = 0
for money, cnt in l:
    total += (money * cnt)
if total == n:
    print("Yes")
else:
    print("No")