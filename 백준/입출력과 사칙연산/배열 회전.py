l = [
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

n = len(l)

for i in l:
    print(i)

for i in range(len(l[0])): # 원래 가로
    for j in range(n):
        print(l[j][i], end=' ')
    print()