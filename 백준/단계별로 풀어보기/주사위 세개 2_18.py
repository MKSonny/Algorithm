import sys
from collections import Counter

li = list(map(int, sys.stdin.readline().split()))
c = Counter(li)

answer = 0
flag = False

for i in c.keys():
    if c[i] == 2:
        answer += 1000 + i * 100
        flag = True
        break
    elif c[i] == 3:
        answer += 10000 + i * 1000
        flag = True
        break

if not flag:
    answer += max(li) * 100

print(answer)