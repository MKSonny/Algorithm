mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

degram = {}
visited = []

for v in mygraph:
    degram[v] = 0

for v in mygraph:
    for u in mygraph[v]:
        degram[u] += 1

for v in mygraph:
    if degram[v] == 0:
        visited.append(v)

while visited:
    start = visited.pop()
    print(start, end=' ')
    for v in mygraph[start]:
        degram[v] -= 1
        if degram[v] == 0:
            visited.append(v)