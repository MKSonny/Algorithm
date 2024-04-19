import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().rstrip().split()))

i = 1
l = [0] * n


while sum(l) != n:
    l = [0] * n
    for item in k:
        for t in range(item - i, item + i):
            if t < 0 or t >= n:
                continue
            if l[t] != 1:
                l[t] = 1
            else:
                continue
    i += 1

print(i - 1)