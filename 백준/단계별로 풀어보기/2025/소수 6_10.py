import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


def check(k):
    for j in range(2, k):
        if k % j == 0:
            return False
    return True


total = 0
minn = 0

for i in range(n, m + 1):
    if check(i):
        if i == 1: continue
        if minn == 0:
            minn = i
        total += i

if total == 0:
    print(-1)
else:
    print(total)
    print(minn)