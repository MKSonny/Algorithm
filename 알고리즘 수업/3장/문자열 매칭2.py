str = ['H', 'E', 'O', 'O', 'O', 'W', 'O', 'R', 'L', 'O']
pattern = ['L', 'O']

def match_string(t, p):
    m = len(p)
    for i in range(len(t) - 1):
        j = 0
        while str[i + j] == pattern[j]:
            j += 1
            if j == m:
                return i
    return -1

idx = match_string(str, pattern)
print(idx)