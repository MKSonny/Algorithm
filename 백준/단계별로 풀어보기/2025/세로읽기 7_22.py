l = []
for _ in range(5):
    l.append(list(input()))



a = [['' for _ in range(5)] for _ in range(15)]

for i in range(5):
    for j in range(len(l[i])):
        a[j][i] = l[i][j]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == '':
            continue
        else:
            print(a[i][j], end='')