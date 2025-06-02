import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

'''
   # 
   #     #
   #   # #
   # # # # #
'''

def calc(y2, y1, x2, x1):
    return (y2 - y1) //(x2 - x1)

def check(x):
    temp = 0
    left_cnt = 0

    for i in range(x - 1, -1, -1):
        prev = calc(l[x], l[i], x, i)

        if prev > temp:
            temp = prev
            left_cnt += 1

    return left_cnt


for i in range(n):
    print(l[i], check(l[i]))
