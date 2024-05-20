import sys
from collections import Counter

n = int(sys.stdin.readline())
l = []
ori = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    ori.append(a)
    l.append(Counter(a))

cnt = 0

for i in range(1, n):
    if abs(len(ori[0]) - len(ori[i])) > 1:
        continue
    a = l[i] - l[0]
    b = l[0] - l[i]
    if len(a) < 2 and len(b) < 2:
        if sum(a.values()) < 2 and sum(b.values()) < 2:
            cnt += 1

print(cnt)
'''
6
ABAAC
ABAA
ABAC
ABAAA
ABCAA
ABSAC
'''