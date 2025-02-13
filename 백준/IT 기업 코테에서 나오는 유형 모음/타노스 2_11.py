import sys

s = list(map(int, sys.stdin.readline().rstrip()))

s.sort()
z_n = s.count(0) // 2
o_n = s.count(1) // 2

q = []


while o_n > 0 or z_n > 0:
    if z_n > 0:
        q.append(0)
        z_n -= 1
    if o_n > 0:
        q.append(1)
        o_n -= 1

if len(s) % 4 != 0:
    q.sort()

for i in q: print(i, end='')
# print(q)