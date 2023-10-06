str = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
pattern = ['L', 'O']

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

idx= string_match(str, pattern)
print(idx)