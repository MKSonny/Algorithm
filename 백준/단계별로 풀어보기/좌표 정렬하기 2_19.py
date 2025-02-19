import sys

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a, b))

li.sort()
for a, b in li: print(a, b)