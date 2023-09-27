import sys
sys.stdin = open('in3.txt', 'r')
number = int(input())
a = [list(map(int, input().split())) for _ in range(number)]

m = number // 2
n = m + 1
print('m, n', m, n)
t = 1
total = 0

for i in range(number):
    if m == 0:
        t = -1

    for j in range(m, n):
        total += a[i][j]

    n = n + (1 * t)
    m = m - (1 * t)
    print('m, n', m, n)

print(total)