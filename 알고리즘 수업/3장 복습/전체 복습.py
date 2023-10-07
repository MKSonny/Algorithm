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

data = [4, 2, 1, 6, 7, 3]
print(data)
selection_sort(data)
print(data)

idx = string_match(str, 'O')
print(idx)