import sys

n, k = map(int, sys.stdin.readline().split())
l = [i for i in range(1, n + 1)]

# 1 2 3 4 5 6 7
# 1 2 4 5 6 7
# 1 2 4 5 7

answer = []
idx = 0
cnt = 0

while l:
    answer.append(l.pop(k - 1))