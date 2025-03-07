import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

'''
10
1000000000 999999999 999999998 999999997 999999996 1 2 3 4 5
'''

def check_left(l, start):
    idx = start - 1

    if l[start] > l[idx]:
        cnt = 1
    else:
        return 1

    cur = idx
    idx = cur - 1

    while idx < n and l[idx] > l[cur]:
        cur = idx
        idx -= 1
        cnt += 1

    return cnt


def check_right(l, start):
    idx = start + 1

    if l[start] > l[idx]:
        cnt = 1
    else:
        return 1

    cur = idx
    idx = cur + 1

    while idx < n and l[idx] > l[cur]:
        cur = idx
        idx += 1
        cnt += 1

    return cnt

for i in range(n - 1):
    print(i, check_left(l, i), check_right(l, i))