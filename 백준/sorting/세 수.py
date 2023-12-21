import sys

input = sys.stdin.readline

h = list(map(int, input().split()))
h.sort()

print(h[1])