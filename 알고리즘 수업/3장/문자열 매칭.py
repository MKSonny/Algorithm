str = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
pattern = ['L', 'O']

def string_matching(T, P):
    l = len(T)
    m = len(P)

    for i in range(l -m + 1):
        j = 0
        while j < m and P[j] == T[i + j]:
            j += 1
        if j == m:
            return i
    return -1

idx = string_matching(str, pattern)
print(idx)