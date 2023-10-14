graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

def dfs(graph, start, v_list):
    if v_list[start] == False:
        print(start, end=' ')
        v_list[start] = True
        nbr = graph[start]
        # print(nbr)
        for i in range(len(nbr)):
            if nbr[i] == 1:
                # print(i)
                # print(v_list)
                dfs(graph, i, v_list)

v_list = [False] * len(graph)
dfs(graph, 0, v_list)