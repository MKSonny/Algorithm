import sys
from collections import deque

n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

total = 0
q = deque()
min_len = float('inf')
flag = False

for i in l:
    total += i
    q.append(i)

    while total >= s:
        flag = True
        min_len = min(min_len, len(q))
        total -= q.popleft()
        # print(q)

if flag:
    print(min_len)
else:
    print(0)
'''
5 1 3 5 10 7 4 9 2 8
5, 1, 3, 5 -> 14
5, 1, 3, 5, 10 -> 24, 15 이상
5를 뺀다
1, 3, 5, 10 -> 19 그래도 15 이상
1을 뺀다

'''