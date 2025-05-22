import sys

n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

l = []

for _ in range(k):
    l.append(int(sys.stdin.readline()))

def dfs_left(i, apple, cnt, s):
    if i < 0:
        return float('inf')
    if i - s <= apple <= i + s:
        return cnt

    cnt += 1

    return dfs_left(i - 1, apple, cnt, s)

def dfs_right(i, apple, cnt, s):
    if i > n:
        return float('inf')
    if i - s <= apple <= i + s:
        return cnt

    cnt += 1

    return dfs_right(i + 1, apple, cnt, s)

start = l.pop(0)

answer = 0

for i in l:
    answer += min(dfs_left(start, i, 0, m - 1), dfs_right(start, i, 0, m - 1))

print(answer)