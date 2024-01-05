n = int(input())
h = []

for _ in range(n):
    m = int(input())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    h.append(matrix)



def dfs(l, level, abil, ssum):
    if level == len(l):
        if all(abil) != True:
            return
        else:
            sum_l.append(ssum)
            return
    for i in range(3):
        ssum += l[level][i]
        abil[i] = True
        dfs(l, level + 1, abil, ssum)
        ssum -= l[level][i]

for l in h:
    total = 0
    for i in l:
        total += sum(i)


    ssum = 0
    sum_l = []
    abil = [0] * 3

    if len(l) < 3:
        print(-1)
    else:
        dfs(l, 0, abil, ssum)
        print(total - max(sum_l))
