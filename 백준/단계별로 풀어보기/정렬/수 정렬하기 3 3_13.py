import sys

l = []
n = int(sys.stdin.readline())
d = {}


for _ in range(n):
    a = int(sys.stdin.readline())

    if a not in d.keys():
        d[a] = 1
    else:
        d[a] += 1


keys = sorted(list(d.keys()))

for key in keys:
    for _ in range(d[key]):
        print(key)