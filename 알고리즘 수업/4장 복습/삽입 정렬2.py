def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

mygraph = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

my_dict = {}

for k in mygraph:
    my_dict[k] = 0

for k in mygraph:
    for v in mygraph[k]:
        my_dict[v] += 1

vlist = []

for k in my_dict:
    if my_dict[k] == 0:
        vlist.append(k)

while vlist:
    v = vlist.pop()
    print(v, end=' ')
    for n in mygraph[v]:
        my_dict[n] -= 1
        if my_dict[n] == 0:
            vlist.append(n)