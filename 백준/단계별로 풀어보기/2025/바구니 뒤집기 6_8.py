import sys

n, m = map(int, sys.stdin.readline().split())
l = [i for i in range(1, n + 1)]


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    temp = []
    for i in range(a - 1, b): # 0, 1
        temp.append(l[i])
    for i in range(a - 1, b):
        l[i] = temp.pop()


for i in l:
    print(i, end=' ')