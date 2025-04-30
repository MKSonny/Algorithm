import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(list(sys.stdin.readline().split()))

for i in l:
    for idx, j in enumerate(i):
        i[idx] = list(j)

t_idx = 0
idx = 0

temp = []

for i in l:
    lt = 0
    rt = -1
    if len(i) > 1:
        rt = 0

    flag = False
    for j in i:
        if flag: break
        if j[0] not in temp:
            temp.append(j[0])
            flag = True
            break
        if rt != -1:
            if j[1][rt] not in temp:
                temp.append(j[1][rt])
                break
        for k in j:
            if k not in temp:
                temp.append(j)
                flag = True
                break

print(temp)