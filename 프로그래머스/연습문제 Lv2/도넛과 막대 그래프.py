def dfs(l, node, node_cnt, edge_cnt, start_node, visited):
    # if node == start_node and node_cnt > 0:
    #     return node_cnt, edge_cnt

    if not visited[node]:
        node_cnt += 1
        visited[node] = True
        # print(node)

    for idx, i in enumerate(l[node]):
        if i == 1:
            # if node != start_node:
            edge_cnt += 1
            l[node][idx] = -1
            return dfs(l, idx, node_cnt, edge_cnt, start_node, visited)


    return node_cnt, edge_cnt


def solution(edges):
    answer = []
    node = max(max(edges))

    l = [[-1 for _ in range(node + 1)] for _ in range(node + 1)]
    for i in range(len(edges)):
        a, b = edges[i]
        l[a][b] = 1

    maxx = -1
    max_i = -1

    for i in range(1, node + 1):
        if maxx < l[i].count(1):
            maxx = l[i].count(1)
            max_i = i

    # dfs(l, node, node_cnt, edge_cnt, start_node)
    # for i in range(1, node + 1):

    # print(l[max_i])

    donut = 0
    graph = 0
    eight = 0

    visited = [False] * (node + 1)
    visited[0] = True

    # while visited.count(True) != node:
    q = []
    for i in range(len(l[max_i])):
        if l[max_i][i] == 1:
            q.append(i)

    # 중심과 연결된 간선의 연결을 모두 끊는다.
    visited[max_i] = True


    while q:
        i = q.pop(0)
        # print(i)
        node_cnt, edge_cnt = dfs(l, i, 0, 0, i, visited)
        if node_cnt == edge_cnt:
            donut += 1
        elif node_cnt == edge_cnt - 1:
            eight += 1
        elif edge_cnt == 0:
            graph += 1
        elif node_cnt == edge_cnt + 1:
            graph += 1
        # print(node_cnt, edge_cnt)

        # if len(q) == 0 and visited.count(True) != node + 1:
        #     temp = visited.index(False)
        #     # print(l[temp])
        #     for idx, i in enumerate(l[temp]):
        #         if i == 1:
        #             # print(i, idx)
        #             visited[idx] = False
        #     q.append(temp)


    # print(donut, eight)
    answer = [max_i, donut, graph, eight]
    # print(answer)
    return answer