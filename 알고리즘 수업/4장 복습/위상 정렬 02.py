mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

my_dict = {}

for key in mygraph:
    my_dict[key] = 0

print(my_dict)

for key in mygraph:
    for value in mygraph[key]:
        my_dict[value] += 1

print(my_dict)

visited = []

for v in my_dict:
    if my_dict[v] == 0:
        visited.append(v)

while visited:
    v = visited.pop()
    print(v, end=' ')
    for u in mygraph[v]:
        my_dict[u] -= 1
        if my_dict[u] == 0:
            visited.append(u)