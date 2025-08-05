import sys

n = int(sys.stdin.readline())


x = 2
while x <= n:
    if n % x == 0:
        print(x)
        n //= x
    else:
        x += 1
