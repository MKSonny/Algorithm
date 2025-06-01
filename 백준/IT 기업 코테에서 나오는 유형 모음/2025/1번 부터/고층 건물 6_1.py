import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

'''
   # 
   #     #
   #   # #
   # # # # #
'''

def check(x):
    lt = x - 2
    rt = x + 2

    left_start = l[x - 1]
    left_cnt = 1

    while lt > 0:
        if l[lt] < left_start:
            left_cnt += 1
            left_start = l[lt]
        lt -= 1

    right_start = l[x + 1]
    right_cnt = 1

    while rt < n:
        if l[rt] < right_start:
            right_cnt += 1
            right_start = l[rt]
        rt += 1

    return left_cnt + right_cnt

for i in range(n):
    print(l[i], check(l[i]))
