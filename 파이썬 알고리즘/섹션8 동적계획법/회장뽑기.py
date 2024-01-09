n = int(input())

l = [[9999 for _ in range(n)] for _ in range(n)]

a = 1
b = 1
'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
'''

while a > 0 and b > 0:
    a, b = map(int, input().split())
    l[a - 1][b - 1] = 1
    l[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                l[i][j] = 0
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

h = []

for i in l:
    h.append(max(i))

minn = min(h)

vote = []
cnt = 0

for i in range(n):
    if minn == h[i]:
        cnt += 1
        vote.append(i + 1)

print(minn, cnt)
for i in range(cnt):
    print(vote[i], end=' ')