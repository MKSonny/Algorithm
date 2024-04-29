import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().rstrip().split()))

def is_safe(l):
    for i in l:
        if i == 0:
            return False
    return True

for i in range(1, n + 1):
    l = [0] * n
    for key in k:
        s = key - i
        e = key + i
        if s < 0:
            s = 0
        if e >= n:
            e = n
        for j in range(s, e):
            if l[j] == 1:
                continue
            l[j] = 1
    if is_safe(l):
        print(i)
        break