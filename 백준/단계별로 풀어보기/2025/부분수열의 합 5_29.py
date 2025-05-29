import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

answer = 0

for w in range(1, len(l) + 1):
    c = combinations(l, w)
    for i in c:
        if sum(i) == s:
            answer += 1

print(answer)