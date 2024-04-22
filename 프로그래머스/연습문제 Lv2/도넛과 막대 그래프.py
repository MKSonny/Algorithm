import copy


def dfs(l, node, start_node, node_cnt, edge_cnt, moved):
    # print('dfs node', node)
    if start_node == node and moved == 1:
        return node_cnt, edge_cnt
    node_cnt += 1
    for idx, item in enumerate(l[node]):
        if item == 1:
            l[node][idx] = -1
            # print('a')
            moved = 1
            edge_cnt += 1
            return dfs(l, idx, start_node, node_cnt, edge_cnt, moved)
    return node_cnt, edge_cnt


def solution(edges):
    answer = []
    node = max(max(edges))

    l = [[-1 for _ in range(node + 1)] for _ in range(node + 1)]
    for i in range(len(edges)):
        a, b = edges[i]
        l[a][b] = 1

    for i in range(1, node + 1):
        print(i)
        temp_l = copy.deepcopy(l)
        print(dfs(temp_l, i, i, 0, 0, 0))

    return answer


# solution([[2, 3], [4, 3], [1, 1], [2, 1]])
# print()
solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])