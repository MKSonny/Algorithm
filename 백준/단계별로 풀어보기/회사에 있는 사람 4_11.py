import sys

n = int(sys.stdin.readline())
d = {}

for _ in range(n):
    name, status = sys.stdin.readline().rstrip().split()
    if status == 'enter':
        d[name] = 1
    else:
        d.pop(name)

d = list(d.keys())
d.sort(reverse=True)

for i in d: print(i)