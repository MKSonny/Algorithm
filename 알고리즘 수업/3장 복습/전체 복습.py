# 선택 정렬
def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[i], a[least] = a[least], a[i]

str = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
pattern = ['L', 'O']

# 문자열 매칭
def string_match(p, t):
    n = len(p)
    m = len(t)
    for i in range(n):
        j = 0
        while p[i + j] == t[j]:
            j += 1
            if j == m:
                return i
    return -1

# 위상 정렬
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

for key in mygraph:
    for value in mygraph[key]:
        my_dict[value] += 1

v_list = []

for key in my_dict:
    if my_dict[key] == 0:
        v_list.append(key)

while v_list:
    v = v_list.pop()
    print(v, end=' ')
    for key in mygraph[v]:
        my_dict[key] -= 1
        if my_dict[key] == 0:
            v_list.append(key)

# data = [4, 2, 1, 6, 7, 3]
# print(data)
# selection_sort(data)
# print(data)
#
# idx = string_match(str, 'O')
# print(idx)