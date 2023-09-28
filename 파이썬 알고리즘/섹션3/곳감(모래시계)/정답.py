import sys
sys.stdin = open('in2.txt', 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
# d = [list(map(int, input().split())) for _ in range(m)]

# 회전
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0))
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

# for k in range(len(d)):
#     row = d[k][0] - 1
#     right = d[k][1]
#     many = d[k][2]
#     for i in range(many):
#         if right:
#             a[row].append(a[row].pop())
#         else:
#             a[row].append(a[row].pop(0))

# 모래 시계 359
s = 0
e = n - 1
total = 0

for i in range(n):
    for j in range(s, e + 1):
        total += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(total)