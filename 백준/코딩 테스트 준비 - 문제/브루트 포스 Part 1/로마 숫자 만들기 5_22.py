import sys

n = int(sys.stdin.readline())
l = [1, 5, 10, 50]

di = {}

for i in range(1, 1001):
    di[i] = 0

answer = []

def dfs(level, total, idx):
    global di
    if level == n:
        di[total] += 1
        return

    for i in range(idx, 4):
        total += l[i]
        dfs(level + 1, total, i)
        total -= l[i]

dfs(0, 0, 0)

cnt = 0

for i in range(1, 1001):
    if di[i] != 0:
        cnt += 1

print(cnt)