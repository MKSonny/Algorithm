import sys

n, m = map(int, sys.stdin.readline().split())
l = []
d = {}

for _ in range(n):
    letter = sys.stdin.readline().rstrip()
    if len(letter) < m:
        continue
    else:
        if d.get(letter) == None:
            d[letter] = 0
        d[letter] += 1

d = list(d.items())
d.sort()
d = sorted(d, key=lambda x: (-x[1], -len(x[0])))

for i in d:
    print(i[0])