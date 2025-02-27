import sys
from collections import deque

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

# l = deque(l)
l.sort()
answer = 0

for i in range(n):
    t = l.pop(i)

    lt = 0
    rt = n - 2
    # print(t, l)

    while lt < rt:
        if l[lt] + l[rt] < t:
            lt += 1
        elif l[lt] + l[rt] == t:
            answer += 1
            break
        else:
            rt -= 1

    l.insert(i, t)

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