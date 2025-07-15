import sys

n = int(sys.stdin.readline())


def fac(t, a):
    if t == 1:
        return a

    a *= t
    fac(t - 1, a)

print(fac(n, 1))