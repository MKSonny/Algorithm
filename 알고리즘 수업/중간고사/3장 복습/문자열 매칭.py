str = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
pattern = ['L', 'O']

def str_find(s, p):
    for i in range(len(s)):
        j = 0
        while s[i + j] == p[j]:
            j += 1
            if j == len(p):
                return i

idx = str_find(str, pattern)
print(idx)