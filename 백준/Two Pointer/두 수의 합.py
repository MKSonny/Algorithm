import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

h = {}

for i in l:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

# print(h)

cnt = 0

for i in l:
    if m - i < 0:
        continue
    else:
        if m - i in h:
            # print('i', i)
            cnt += h[m - i]

print(cnt//2)