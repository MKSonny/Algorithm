import copy
import sys

n, k = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().rstrip())
cnt = 0

for i in range(n):
    if l[i] == 'P':
        for m in range(max(i - k, 0), min(i + k + 1, n)):
            if l[m] == 'H':
                l[m] = 'x'
                l[i] = 'u'
                cnt += 1
                break

print(cnt)