data = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
res = [0] * 3
max_total = 0
def dfs(l, s):
    global max_total
    if l == 3:
        t = 0
        for item in res:
            t += item
        if max_total < t and t < 500:
            max_total = t
    else:
        for i in range(s, len(data)):
            res[l] = data[i]
            dfs(l + 1, i + 1)

dfs(0, 0)
print(max_total)