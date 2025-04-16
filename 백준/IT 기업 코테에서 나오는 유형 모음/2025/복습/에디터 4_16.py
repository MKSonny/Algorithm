import sys
from collections import deque

left = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
cur = len(left)

right = deque([])

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if len(command) > 1:
        a = command[0]
        b = command[2]
        if a == 'P':
            left.append(b)
    else:
        a = command[0]
        if a == 'L':
            if len(left) == 0: continue
            right.appendleft(left.pop())
        elif a == 'D':
            if len(right) == 0: continue
            left.append(right.popleft())
        elif a == 'B':
            if len(left) == 0: continue
            left.pop()

word = left + list(right)
print(''.join(word))