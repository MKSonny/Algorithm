list = [1, 3, 5, 6, 7, 10]
n = len(list)
total = sum(list)

def dfs(l, s):
    if l == n:
        if s == total - s:
            print('YES')
    else:
        dfs(l + 1, s + list[l])
        dfs(l + 1, s)

dfs(0, 0)