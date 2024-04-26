k, n = map(int, input().split())
l = []

for _ in range(k):
    l.append(int(input()))

def find(l, first, last, n, maxx):
    while last >= first:
        mid = (first + last) // 2
        total = 0
        for i in l:
            total += i // mid
        if total >= n:
            maxx = mid
            first = mid + 1
            # return find(l, first, last, n, maxx)
        # if total > n:
        #     first = mid + 1
            # return find(l, first, last, n, maxx)
        else:
            last = mid - 1
            # return find(l, first, last, n, maxx)
    # else:
    return maxx
'''
4 11
802
743
457 
539

10695848
'''
print(find(l, 1, max(l), n, -1))