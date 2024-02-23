import copy

n = int(input())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

h = copy.deepcopy(l)
# for i in l:
#     print(i)

cnt = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if k != i and k != j:
                if l[i][k] + l[k][j] == l[i][j]:
                    l[i][j] = float('inf')
                    # flag = True
                    # print(k + 1, i + 1, j + 1)
                    # cnt += 1
ssum = 0

for i in range(n):
    for j in range(n):
        if l[i][j] != float('inf'):
            ssum += l[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] + l[k][j] < l[i][j]:
                # flag = False
                l[i][j] = l[i][k] + l[k][j]
#
# for i in l:
#     print(i)
#
# print(cnt)




if h == l:
    print(ssum // 2)
else:
    print(-1)