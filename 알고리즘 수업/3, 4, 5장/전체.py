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

data = [4, 1, 3, 9, 10, 2]

def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if a[least] > a[j]:
                least = j
        a[i], a[least] = a[least], a[i]

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

# dfs(mygraph, 'A', set())
# bfs(mygraph, 'A')

mygraph2 = {
    'A' : {'C', 'D'},
    'B' : {'D', 'E'},
    'C' : {'D', 'F'},
    'D' : {'F'},
    'E' : {'F'},
    'F' : {}
}

def topology_sort(graph):
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
        v = v_list.pop()
        print(v, end=' ')
        for n in graph[v]:
            my_dict[n] -= 1
            if my_dict[n] == 0:
                v_list.append(n)


# topology_sort(mygraph2)

def insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

# insertion_sort(data)
# print(data)

def binary_search(a, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            return binary_search(a, left, mid - 1, key)
        else:
            return binary_search(a, mid + 1, right, key)

# print(binary_search(data, 0, len(data) - 1, 2))

def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)


# print(power(5, 4))
def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right

    while low <= high:
        while low <= right and a[low] < pivot: low += 1
        while high >= left and a[high] > pivot: high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

    a[left], a[high] = a[high], a[left]

    return high

def quick_select(a, left, right, k):
    pos = partition(a, left, right)
    if pos + 1 == left + k:
        return a[pos]
    elif pos + 1 > left + k:
        return quick_select(a, left, pos - 1, k)
    else:
        return quick_select(a, pos + 1, right, left - (pos + 1) + k)

# print(data)
# print(quick_select(data, 0, len(data) - 1, 5))

def merge(a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    sorted = [0] * len(a)
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = a[j]
            j, k = j + 1, k + 1
    if i > mid:
        # 아래처럼 해도 결과가 잘 나온다...
        # sorted[k : right + 1] = a[j : right + 1]
        sorted[k : k + right - j + 1] = a[j : right + 1]
    else:
        sorted[k : right + 1] = a[i : mid + 1]

    a[left : right + 1] = sorted[left : right + 1]

def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)

def quick_sort(a, left, right):
    if left < right:
        pos = partition(a, left, right)
        quick_sort(a, left, pos - 1)
        quick_sort(a, pos + 1, right)


print(data)
# merge_sort(data, 0, len(data) - 1)
quick_sort(data, 0, len(data) - 1)
print(data)

def mul_mat(a, b):
    temp = [([0] * len(b[0])) for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b[0])):
            sum = 0
            for j in range(len(a[0])):
                sum += a[i][j] * b[j][k]
            temp[i][k] = sum

    return temp

def power_mat(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power_mat(mul_mat(x, x), n // 2)
    else:
        return mul_mat(x, power_mat(mul_mat(x, x), (n - 1) // 2))

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6, 7],
    [8, 9, 10]
]

result = power_mat(a, 3)
print(result)

'''
4. 축소 정복 기법 -> 모든 경우의 수(상향식, 하향식)
    1. 삽입 정렬
    2. 위상 정렬
    3. 이진 탐색
    4. 거듭제곱 문제
    5. k번째 작은 수 찾기
5. 분할 정복 기법
    1. 병합 정렬
    2. 퀵 정렬
'''