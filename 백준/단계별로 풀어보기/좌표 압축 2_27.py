import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
d = {}

t = l[:]
t = list(set(t))
t.sort()


for i in l:
    if i not in d.keys():
        d[i] = 0

for i in range(len(t)):
    d[t[i]] = i

for i in l:
    print(d[i], end=' ')