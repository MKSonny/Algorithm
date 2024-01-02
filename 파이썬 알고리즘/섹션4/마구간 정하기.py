n, m = map(int, input().split())
l = []
'''
5 3
1
2
8
4
9
'''

for _ in range(n):
    l.append(int(input()))

l.sort()


def binary_search(l, lt, rt, key):
    res = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        ep = l[0]
        for i in range(1, n):
            if l[i] - ep >= mid:
                ep = l[i]
                cnt += 1

        # print(cnt, mid)

        if cnt >= key:
            res = mid
            # print('res', res)
            lt = mid + 1
        else:
            rt = mid - 1

    return res



print(binary_search(l, 1, l[n - 1], m))