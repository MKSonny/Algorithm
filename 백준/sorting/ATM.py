import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
h.sort()
total = 0

for i in range(n):
    total += sum(h[0:i + 1])

print(total)