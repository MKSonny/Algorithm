n = int(input())

'''
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4
'''
#

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

sum_a = 0
sum_b = 0

for j in range(n):
    sum_a += l[0][j]
    sum_b += l[j][0]
    l[0][j] = sum_a
    l[j][0] = sum_b

for i in range(1, n):
    for j in range(1, n):
        l[i][j] = min(l[i - 1][j] + l[i][j], l[i][j - 1] + l[i][j])

for i in l:
    print(i)