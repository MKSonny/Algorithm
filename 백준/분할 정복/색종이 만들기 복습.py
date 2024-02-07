import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))


blue_cnt = 0
white_cnt = 0

def devide(l, start, end):
    temp = l[start][end]
    for i in range(n):
        for j in range(n):
            if temp != l[i][j]:
                

devide(l, n)
print(blue_cnt)
print(white_cnt)
