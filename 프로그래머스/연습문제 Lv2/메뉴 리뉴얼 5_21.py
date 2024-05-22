l = [['W', 'X', 'Y'], ['A', 'W', 'X']]


def dfs(level, concept, find):
    print(l[level][find])
    if level == 2:
        find += 1
        return

    for i in range(3):
        
        dfs(level + 1, concept, find)

dfs(0, 0, 0)