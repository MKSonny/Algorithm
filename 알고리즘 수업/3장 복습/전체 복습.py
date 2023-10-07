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
# mygraph = {
#     'A' : {'C', 'D'},
#     'B' : {'D', 'E'},
#     'C' : {'D', 'F'},
#     'D' : {'F'},
#     'E' : {'F'},
#     'F' : {}
# }
#
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
#     for key in mygraph[v]:
#         my_dict[key] -= 1
#         if my_dict[key] == 0:
#             v_list.append(key)

# 이진 탐색
def binary_search(a, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return binary_search(a, left, mid - 1, key)
        else:
            return binary_search(a, mid + 1, right, key)

# k번째 작은 수 찾기
def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right
    while low <= high:
        while low <= right and a[low] < pivot:
            low += 1
        while high >= left and a[high] > pivot:
            high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]
    if low > high:
        a[left], a[high] = a[high], a[left]
    return high
def find(a, left, right, k):
    pivot = partition(a, left, right)
    print('left:', left)
    print('k:', k)
    print('left + k =', left + k)
    if pivot + 1 == left + k:
        return a[pivot]
    elif pivot + 1 > left + k:
        return find(a, left, pivot - 1, k)
    else:
        return find(a, pivot + 1, right, k - (pivot + 1 - left))


data = [1, 2, 3, 4, 5, 6]
num = find(data, 0, len(data) - 1, 6)
print(num)
# idx = binary_search(data, 0, len(data) - 1, 2)
# print(idx)

# data = [4, 2, 1, 6, 7, 3]
# print(data)
# selection_sort(data)
# print(data)
#
# idx = string_match(str, 'O')
# print(idx)