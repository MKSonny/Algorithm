import sys

n = int(sys.stdin.readline())

lo = list(map(int, sys.stdin.readline().split()))

stack = []
ans = [0] * n

for i in range(n):
    while stack:
        if stack[-1][1] > lo[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, lo[i]))

print(*ans)