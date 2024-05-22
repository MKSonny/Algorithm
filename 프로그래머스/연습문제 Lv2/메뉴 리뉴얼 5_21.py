l = [['X', 'Y', 'Z'], ['A', 'W', 'X'], ['W', 'X', 'Y']]
# 13:57
found = []
def dfs(level, c, f, prev, found):
    # global found
    # print(l[level])
    if f == 3:
    if level == len(l):
        return
    print(l[level], level, c, f, prev, found)
    f_idx = 0
    idx = prev
    while found:
        # print(f_idx, idx, l[level])
        if idx >= len(l[level]):
            break
        if found[f_idx] == l[level][idx]:
            f_idx += 1
            if f_idx >= len(found):
                break
        idx += 1

    if f_idx != 0:
        prev = idx - 1
        # print('work', prev)

    for i in range(prev, len(l[level])):
        if l[c][f] == l[level][i]:
            found.append(l[c][f])
            dfs(level, c, f + 1, i + 1, found)
    dfs(level + 1, c, f, 0, found)

dfs(1, 0, 0, 0, [])
print('found', found)