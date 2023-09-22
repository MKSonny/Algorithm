list = [81, 58, 42, 33, 61]
max = 259
n = len(list)
total_list = []
real_max = -1

def dfs(l, s):
    global real_max
    if s > max:
        return
    if l == n:
        if real_max < s:
            real_max = s
    else:
        dfs(l + 1, list[l] + s)
        dfs(l + 1, s)

dfs(0, 0)
print(real_max)