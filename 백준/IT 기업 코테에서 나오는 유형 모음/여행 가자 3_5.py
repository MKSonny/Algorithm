import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[] for _ in range(n)]

for idx in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    for k_idx in range(len(k)):
        if k[k_idx] == 1:
            l[idx].append(k_idx)

print(l)