import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))


def bubble_sort(l):
    n = len(l)
    cnt = 0

    for i in range(n):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                cnt += 1
                l[j], l[j + 1] = l[j + 1], l[j]

    print(cnt)


idx = 1

for item in l:
    print(idx, end=' ')
    bubble_sort(item[1:])
    idx += 1