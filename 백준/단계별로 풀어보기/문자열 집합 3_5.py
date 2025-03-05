import sys

n, m = map(int, sys.stdin.readline().split())
s = []
t = []

for _ in range(n):
    s.append(sys.stdin.readline().rstrip())

cnt = 0

for _ in range(m):
    a = sys.stdin.readline().rstrip()

    if a in s:
        cnt += 1

print(cnt)