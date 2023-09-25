string = ['A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M']
n = len(string)
for i in range(n - 1):
    least = i
    for j in range(i + 1, n):
        if string[least] > string[j]:
            least = j
    string[i], string[least] = string[least], string[i]

print(string)