import sys
sys.stdin = open('in1.txt', 'r')
number = int(input())
a = [list(map(int, input().split())) for _ in range(number)]
n = len(a)
# 6x6 이차원 배열 생성
temp = [[0] * (number + 2) for _ in range(number + 2)]

for i in range(1, number + 1):
    for j in range(1, number + 1):
        temp[i][j] = a[i - 1][j - 1]

for row in temp:
    print(row)

cnt = 0

for i in range(1, number + 1):
    for j in range(1, number + 1):
        key = temp[i][j]
        up = i - 1
        down = i + 1
        left = j - 1
        right = j + 1
        if key > temp[up][j] and key > temp[down][j] and key > temp[i][left] and key > temp[i][right]:
            cnt += 1

print(cnt)