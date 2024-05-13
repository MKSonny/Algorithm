import copy
import sys

n, k = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().rstrip())
cnt_1 = 0
cnt_2 = 0
l2 = copy.deepcopy(l)

for m in range(k, 0, -1):
    for i in range(n):
        if l[i] == 'P':
            if i - m >= 0 and l[i - m] == 'H':
                l[i - m] = 'x'
                l[i] = 'U'
                cnt_1 += 1
            elif i + m < n and l[i + m] == 'H':
                l[i + m] = 'x'
                l[i] = 'U'
                cnt_1 += 1

for m in range(1, k + 1):
    for i in range(n):
        if l2[i] == 'P':
            if i - m >= 0 and l2[i - m] == 'H':
                l2[i - m] = 'x'
                l2[i] = 'U'
                cnt_2 += 1
            elif i + m < n and l2[i + m] == 'H':
                l2[i + m] = 'x'
                l2[i] = 'U'
                cnt_2 += 1

print(max(cnt_1, cnt_2))