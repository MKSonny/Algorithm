import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

a = a * b * c

a = list(map(int, str(a)))

l = [0 for _ in range(10)]

for i in a:
    l[i] += 1

for i in l:
    print(i)