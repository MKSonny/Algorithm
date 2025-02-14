plus_visited = [False] * 4

# F F F F
# T F F F
# T T F F
# T T T F
# T T T T
# F T F F


def dfs(vi, level):
    if level == 4:
        print(vi)
        return
    for i in range(4):
        if not vi[i]:
            vi[i] = True
            dfs(vi, level + 1)
            vi[i] = False

dfs(plus_visited, 0)