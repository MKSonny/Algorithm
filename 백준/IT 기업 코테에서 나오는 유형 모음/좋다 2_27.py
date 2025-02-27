import sys
from itertools import combinations

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))
answer = 0

for idx in range(n):
    t = l.pop(0)
    c = combinations(l, 2)
    options = set()

    for i in c:
        options.add(i[0] + i[1])

    if t in options:
        answer += 1

    l.append(t)

print(answer)


'''
5
-1 0 1 2 3
lt = 0
rt = 3
mid = 1

-1 + 2 = 1 < 3
lt = mid + 1
lt = 1
rt = 3

0[1] + 2[3] = 2 < 3
lt = mid + 1 -> 3 
rt = 3

=========
lt = 0
rt = 3
mid = 1

lt = mid
lt = 1
rt = 3

lt = mid = 2
rt = 3
1[2] + 2[3] = 3 찾음
자기 자신은 제외해야 한다
'''