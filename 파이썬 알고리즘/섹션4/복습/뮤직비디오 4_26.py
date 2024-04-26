n, m = map(int, input().split())
l = list(map(int, input().split()))

def find(l, first, last, m):
    result = 0
    while last >= first:
        mid = (first + last) // 2
        total, cnt = 0, 1
        for i in l:
            total += i
            if total > mid:
                cnt += 1
                total = i
                # print(mid, total)


        # cnt += 1
        if cnt <= m:
            # print('r', result)
            result = mid
            last = mid - 1
        else:
            first = mid + 1

    return result

'''
9 3 
1 2 3 4 5 6 7 8 9
469
515
'''

print(find(l, 1, sum(l), m))