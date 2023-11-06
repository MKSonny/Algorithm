def dfs(S, M, value, level, remaining):
    if level == 4:
        return
    if sum(S) == M:
        return S

    for i in range(level, len(value)):
        S.append(value[i]) # 1, 2 # 1, 3
        dfs(S, M, level + 1, remaining - S[i])
        S.pop() # 1, pop(2)