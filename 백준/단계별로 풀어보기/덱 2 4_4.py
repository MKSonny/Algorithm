import sys
from collections import deque

n = int(sys.stdin.readline())
l = deque()

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a) > 1:
        a, b = a.split()
        if a == '1':
            l.appendleft(b)
            continue
        elif a == '2':
            l.append(b)
            continue
    else:
        if a == '3':
            if len(l):
                print(l.popleft())
            else:
                print(-1)
        elif a == '4':
            if len(l):
                print(l.pop())
            else:
                print(-1)
        elif a == '5':
            print(len(l))
        elif a == '6':
            if len(l) == 0:
                print(1)
            else:
                print(0)
        elif a == '7':
            if len(l):
                print(l[0])
            else:
                print(-1)
        elif a == '8':
            if len(l):
                print(l[-1])
            else:
                print(-1)
