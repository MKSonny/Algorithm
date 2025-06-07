import sys

n = int(sys.stdin.readline())

'''
1 -> 1/1
2 -> 1/2
3 -> 2/1
4 -> 3/1
5 -> 2/2
6 -> 1/3
7 -> 1/4

1, 2, 6, 7, 15
'''
# [1, 2(2, 3), 3(4, 5, 6), 4(7, 8, 9, 10), 5]
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    print(str(n) + '/' + str(line - n + 1))
else:
    print(str(line - n + 1) + '/' + str(n))