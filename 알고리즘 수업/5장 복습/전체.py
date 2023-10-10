'''
3. 억지기법과 완전 탐색
    1. 선택 정렬
    2. 순차 탐색
    3. 문자열 매칭
    4. 최근접 쌍의 거리
    5. 완전 탐색
    6. 그래프 탐색 (DFS, BFS)
'''
import queue

data = [4, 1, 3, 9, 21]

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[least], a[i] = a[i], a[least]

str = list('hello world')
pat = 'a'

def string_match(t, p):
    n = len(t)
    m = len(p)
    for i in range(n):
        j = 0
        while t[i + j] == p[j]:
            j += 1
            if j == m:
                return i
    return -1

idx = string_match(str, pat)
print(idx)

# print(data)
# selection_sort(data)
# print(data)

mygraph = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A", "D", "E"},
    "D": {"B", "C", "F"},
    "E": {"C", "G", "H"},
    "F": {"D"},
    "G": {"E", "H"},
    "H": {"E", "G"}
}

mygraph_t = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

def bfs(graph, start):
    visited = { start }
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        print(v, end=' ')
        nbr = graph[v] - visited
        for n in nbr:
            q.put(n)
            visited.add(n)

dfs(mygraph, 'A', set())
print()
bfs(mygraph, 'A')
'''
4. 축소 정복 기법
    1. 삽입 정렬
    2. 위상 정렬
    3. 이진 탐색
    4. 거듭제곱 문제
    5. k번째 작은 수 찾기
'''

def topological_sort(graph):
    my_dict = {}
    for key in graph:
        my_dict[key] = 0

    for k in graph:
        for v in graph[k]:
            my_dict[v] += 1

    v_list = []

    for k in my_dict:
        if my_dict[k] == 0:
            v_list.append(k)

    while v_list:
        n = v_list.pop()
        print(n, end=' ')
        for v in graph[n]:
            my_dict[v] -= 1
            if my_dict[v] == 0:
                v_list.append(v)

print()
topological_sort(mygraph_t)

def insertion_sort(a):
    n = len(a)
    for i in range(n):
        j = i - 1
        key = a[i]

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

def binary_search(a, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            return binary_search(a, mid + 1, right, key)
        else:
            return binary_search(a, left, mid - 1, key)
print('ch04')
insertion_sort(data)
print(data)
idx = binary_search(data, 0, len(data) - 1, 2)
print(idx)

def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right

    while low <= high:
        while low <= right and a[low] <= pivot:
            low += 1
        while high >= left and a[high] > pivot:
            high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

    # if low > high:
    a[left], a[high] = a[high], a[left]

    return high

def find_k(a, left, right, k):
    pos = partition(a, left, right)
    if pos + 1 == left + k:
        return a[pos]
    elif pos + 1 > left + k:
        return find_k(a, left, pos - 1, k)
    else:
        return find_k(a, pos + 1, right, left - (pos + 1) + k)

print()
insertion_sort(data)
print(data)
n = find_k(data, 0, len(data) - 1, 2)
print(n)
# insertion_sort_recur(data, len(data))
# print(data)
'''
5. 분할 정복 기법
    1. 병합 정렬
    2. 퀵 정렬
'''