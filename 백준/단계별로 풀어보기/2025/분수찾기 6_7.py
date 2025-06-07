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
cnt = 1
g = 1
g_cnt = 0

i, j = 1, 1
toggle = False

while True:
    if cnt == n:
        # print(g, n, i, j)
        print(str(i) + '/' + str(j))
        break

    g_cnt += 1

    if toggle:
        j -= 1
        i += 1
    else:
        j += 1
        i -= 1

    if g_cnt == g:
        toggle = not toggle
        g += 1
        g_cnt = 0

        if toggle:
            j = g
            i = 1
        else:
            i = g
            j = 1

    cnt += 1