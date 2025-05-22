import sys

a, b, v = map(int, sys.stdin.readline().split())

if ((v - b) / (a - b)) - ((v - b) // (a - b)) != 0:
    print((v - b) // (a - b) + 1)
else:
    print((v - b) // (a - b))