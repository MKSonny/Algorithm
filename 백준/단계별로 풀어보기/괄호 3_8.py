import sys
from collections import deque

n = int(sys.stdin.readline())

def check(l):
    s = []
    while l:
        a = l.popleft()
        if a == '(':
            s.append(a)
        else:
            if len(s) == 0:
                return False
            b = s.pop()
            if b != '(':
                return False

    if s: return False
    return True

for _ in range(n):
    t = deque(list(sys.stdin.readline().rstrip()))
    if check(t):
        print('YES')
    else:
        print('NO')