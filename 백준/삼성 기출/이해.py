visited = [False, False, False]
cnt = 0
def dfs(pick):
    global cnt
    cnt += 1
    print(cnt, visited)
    if pick == 2:
        return


    # i: 0, 1, 2
    for i in range(3):
        if visited[i] == False:
            visited[i] = True
            dfs(pick + 1)
            visited[i] = False

dfs(0)