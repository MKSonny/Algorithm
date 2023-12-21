import heapq
import sys

input = sys.stdin.readline
n = int(input())

h = []

for _ in range(n):
    m = int(input())
    h.append(m)

h.sort()

while h:
    print(h.pop(0))