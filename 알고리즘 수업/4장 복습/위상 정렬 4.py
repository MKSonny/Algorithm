mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

def topological_sort(graph):
    my_dict = {}
    for k in graph:
        my_dict[k] = 0

    for k in graph:
        for v in graph[k]:
            my_dict[v] += 1

    v_list = []

    for k in my_dict:
        if my_dict[k] == 0:
            v_list.append(k)

    while v_list:
        v = v_list.pop()
        print(v, end=' ')
        for n in graph[v]:
            my_dict[n] -= 1
            if my_dict[n] == 0:
                v_list.append(n)


topological_sort(mygraph)