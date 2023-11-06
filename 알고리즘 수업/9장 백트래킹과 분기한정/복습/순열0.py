def dfs(data, sol, visited):
    for i in range(len(data)):
        if visited[i] == 0:
            sol.append(data[i])
            visited[i] = True
            dfs(data, sol, visited)
            visited[i] = False
            sol.pop()