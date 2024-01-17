n = int(input())
f = list(map(int, input().split()))

m = int(input())
s = list(map(int, input().split()))

f.sort()
s.sort()
h = []

while f and s:
    if f[0] < s[0]:
        h.append(f.pop(0))
    else:
        h.append(s.pop(0))

if s:
    while s:
        h.append(s.pop(0))
else:
    while f:
        h.append(f.pop(0))

print(h)