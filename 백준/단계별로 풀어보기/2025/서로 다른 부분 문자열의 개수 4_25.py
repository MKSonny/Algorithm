import sys

l = list(sys.stdin.readline().rstrip())
n = len(l)

d = {}

for i in range(n):
    for j in range(1, n - i + 1):
        temp = ''.join(l[i:i + j])
        if temp not in d.keys():
            d[temp] = 1
        else:
            d[temp] += 1

print(len(d.keys()))