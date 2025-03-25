import sys
from collections import deque

n = int(sys.stdin.readline())
l = deque(list(map(int, sys.stdin.readline().split())))

seq = 1

line = []
t = []


flag_1 = False
flag_2 = False

while seq != n + 1:
    flag_1 = False
    flag_2 = False

    while len(l):
        a = l.popleft()
        if a == seq:
            seq += 1
            flag_1 = True
            break
        else:
            t.append(a)

    while len(t) and t[-1] == seq:
        seq += 1
        flag_2 = True
        t.pop()
        if len(t) == 0:
            break

    if not flag_1 and not flag_2:
        break


if seq == n + 1:
    print('Nice')
else:
    print('Sad')