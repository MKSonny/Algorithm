import sys
import math

n = int(sys.stdin.readline())

def check(a, b):
    return math.lcm(a, b)

# 1 2 3 5 6 10 15 30

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(check(a, b))
