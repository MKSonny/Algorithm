n, m = map(int, input().split())
l = []
'''
4 11
802
743
457
539
'''

for _ in range(n):
    l.append(int(input()))

l.sort()

def binary_find(l, key, low, high):
    max_length = 0
    while low <= high:
        cnt = 0
        mid = (low + high) // 2

        for k in l:
            cnt += k // mid

        # print(cnt)

        if cnt >= key:
            if mid > max_length:
                max_length = mid
            # print(max_length)
            low = mid + 1
            # return mid
        else:
            high = mid - 1

    return max_length

print(binary_find(l, m, 0, l[n - 1]))