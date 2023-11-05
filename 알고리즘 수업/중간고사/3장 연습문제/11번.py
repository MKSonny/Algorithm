string = 'ADBAAEDBA'
data = list(string)
print(data)
def count_substr(str, A, B):
    count = 0
    n = len(str)
    for i in range(n - 1):
        if str[i] == A:
            for j in range(i + 1, n):
                if str[j] == B:
                    count += 1
    return count

asw = count_substr(string, 'A', 'B')
print(asw)