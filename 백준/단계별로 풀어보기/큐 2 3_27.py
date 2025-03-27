import sys
from collections import deque

n = int(sys.stdin.readline())
s = deque([])

for _ in range(n):
    a = sys.stdin.readline().rstrip().split()

    c = a[0]

    if len(a) > 1:
        b = a[1]

    if c == 'push':
        s.append(b)
    elif c == 'pop':
        if len(s) == 0:
            print(-1)
            continue
        print(s.popleft())
    elif c == 'front':
        if len(s) == 0:
            print(-1)
            continue
        print(s[0])
    elif c == 'back':
        if len(s) == 0:
            print(-1)
            continue
        print(s[-1])
    elif c == 'empty':
        if len(s) > 0:
            print(0)
        else:
            print(1)
    elif c == 'size':
        print(len(s))