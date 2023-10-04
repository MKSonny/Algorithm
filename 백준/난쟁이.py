import sys

a = []

for i in range(9):
    a.append(int(input()))

res = [0] * 7

def dfs(l, s):
    if l == 7:
        total = 0
        for item in res:
            total += item
        if total == 100:
            for item in res:
                print(item)
    else:
        for i in range(s, 9):
            res[l] = a[i]
            dfs(l + 1, i + 1)

dfs(0, 0)