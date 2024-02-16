n, r, c = map(int, input().split())

'''
0, 0
0, 1
1, 0
1, 1

0, 2
0, 3
1, 2
1, 3
'''
def z(l, y, x, cnt):
    # 하나의 반복은?
    for i in range(n):
        for j in range(n):
            l[i][j] = cnt
            cnt += 1
            if cnt % 4 == 0:
                z(l, )

l = [0] * (n ** 2)
z(l, 0, 0, 0)