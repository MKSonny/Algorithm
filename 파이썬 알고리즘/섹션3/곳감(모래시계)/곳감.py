import sys
sys.stdin = open('in1.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
d = [list(map(int, input().split())) for _ in range(m)]

# 회전
for k in range(len(d)):
    row = d[k][0] - 1
    right = d[k][1]
    many = d[k][2]
    temp = a[row][:]
    print('temp', temp[-3])

    for i in range(n):
        idx = i + many
        if idx > n - 1:
            idx %= n
        if right:
            a[row][i] = temp[idx - 1]
        else:
            a[row][i] = temp[idx]

# 모래 시계 359
s = 0
e = n
total = 0

for i in range(n):
    for j in range(s, e):
        total += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

for row in a:
    print(row)

print(total)
print(temp)