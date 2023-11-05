def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

# B E A C D F
# 아래 그래프로 하면 틀림
mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F', 'A'},
    'D' : {'F', 'A', 'B', 'C'},
    'E' : {'F', 'B'},
    'F' : {'C', 'D', 'E'}
}

# my_dict = {}
#
# for key in mygraph:
#     my_dict[key] = 0
#
# for key in mygraph:
#     for value in mygraph[key]:
#         my_dict[value] += 1
#
# v_list = []
#
# for key in my_dict:
#     if my_dict[key] == 0:
#         v_list.append(key)
#
# while v_list:
#     v = v_list.pop()
#     print(v, end=' ')
#     for n in mygraph[v]:
#         my_dict[n] -= 1
#         if my_dict[n] == 0:
#             v_list.append(n)

dfs(mygraph, 'B', set())