def string_match(t, p):
    n = len(t)
    m = len(p)
    k = 0

    for i in range(n):

        if t[i] == p[k]:
            k += 1
        else:
            k = 0

        # k 증가 후 검사 해야 하니까
        if k == m:
            return i - m + 1

    return -1

str = ['H', 'E', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'K']
pattern = ['L', 'O']

idx = string_match(str, pattern)
print(idx)