import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a = list(sys.stdin.readline().rstrip())
    a.sort()
    l.append(set(a))

cnt = 0

for i in range(1, n):
    if l[0] == l[i]:
        cnt += 1

print(cnt)