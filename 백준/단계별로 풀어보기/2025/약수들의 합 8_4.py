import sys

l = []
while True:
    n = int(sys.stdin.readline())
    l.append(n)
    if n == -1:
        break

def check(n):
    a = []

    for i in range(1, n):
        if n % i == 0:
            a.append(i)

    if sum(a) == n:
        print(str(n) + ' = ', end='')
        for i in range(len(a) - 1):
            print(str(a[i]), end=' + ')
        print(a[-1])
    else:
        print(str(n) + ' is NOT perfect.')


for i in l:
    if i == -1: break
    check(i)