import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
min_l = min(l)
max_l = max(l)


def check(nx):
    if min_l <= nx <= max_l and (nx in l) and (nx not in A):
        A.append(nx)
        return 1
    return 0


def dfs(x):
    if x % 3 == 0:
        if check(x // 3):
            return dfs(x // 3)
        if check(x * 2):
            return dfs(x * 2)
    else:
        if check(x * 2):
            return dfs(x * 2)


for x in l:
    A = [x]
    dfs(x)
    if len(A) == len(l):
        print(*A, end=' ')
        break