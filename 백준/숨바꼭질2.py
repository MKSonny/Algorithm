# x - 1 or x + 1 or 2x
# 5 17
cnt = 0
min_time = 99999
str = input()
n, m = map(int, str.split())
time = []

def dfs(l, n, m):
    global min_time
    global cnt

    if l == 0:
        dfs(l + 1, n + 1, m)
        dfs(l + 1, n - 1, m)
        dfs(l + 1, 2 * n, m)
        # test

    else:
        if n < m:
            dfs(l + 1, n + 1, m)
            dfs(l + 1, 2 * n, m)
        elif n == m:
            time.append(l)
            if min_time > l:
                min_time = l
            return
        else:
            dfs(l + 1, n - 1, m)

dfs(0, 5, 17)
for item in time:
    if item == min_time:
        cnt += 1
print(min_time, cnt)