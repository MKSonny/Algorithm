import sys

n = int(sys.stdin.readline())
s = []

for _ in range(n):
    t = int(sys.stdin.readline())
    if t == 0:
        s.pop()
    else:
        s.append(t)

print(sum(s))