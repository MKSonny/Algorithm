def get_parent(parent, x):
    if parent[x] == x:
        return x
    return get_parent(parent, parent[x])

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return 1
    return 0

parent = []
for i in range(10):
    parent.append(i)

union_parent(parent, 1, 2)
union_parent(parent, 2, 3)
union_parent(parent, 3, 4)
union_parent(parent, 5, 6)
union_parent(parent, 6, 7)
union_parent(parent, 7, 8)
union_parent(parent, 8, 9)

print(parent)