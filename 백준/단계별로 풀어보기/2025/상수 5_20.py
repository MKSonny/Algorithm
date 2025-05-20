import sys

n, m = sys.stdin.readline().rstrip().split()

n, m = list(n), list(m)

n = int(''.join(n[::-1]))
m = int(''.join(m[::-1]))

print(max(n, m))