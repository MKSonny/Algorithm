def count(string):
    cnt = 0
    n = len(string)
    for i in range(n - 1):
        if string[i] == 'A':
            for j in range(i + 1, n):
                if string[j] == 'B':
                    cnt += 1
    return cnt

print(count(list('ADBAAEDBA')))