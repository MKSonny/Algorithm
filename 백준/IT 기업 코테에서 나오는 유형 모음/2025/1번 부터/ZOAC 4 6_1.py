import sys

h, w, n, m = map(int, sys.stdin.readline().split())

if h % (n + 1) != 0:
    h += 1
if w % (m + 1) != 0:
    w += 1

print((h // (n + 1)) * (w // (m + 1)))