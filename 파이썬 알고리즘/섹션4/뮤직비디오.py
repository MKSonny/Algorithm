n, m = map(int, input().split())
l = list(map(int, input().split()))

'''
9 3
1 2 3 4 5 6 7 8 9

9 9
1 2 3 4 5 6 7 8 9
'''

lt = l[0]
rt = sum(l)

maxx = max(l)

def binary_cnt(l, lt, rt, key):
    min = 0
    while lt <= rt:
        mid = (lt + rt) // 2

        cnt = 0
        total = 0

        for k in l:
            cnt += k
            if cnt > mid:
                total += 1
                cnt = k

        total += 1
        # print(total)

        if mid >= maxx and total <= key:
            min = mid
            rt = mid - 1
        else:
            lt = mid + 1

    return min

print(binary_cnt(l, lt, rt, m))