import sys

l = []
total = 0
for _ in range(5):
    a = int(sys.stdin.readline())
    l.append(a)
    total += a

print(total // 5)
l.sort()
print(l[5 // 2])