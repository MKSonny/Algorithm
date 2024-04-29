'''
5 4
1
2
8
4
9
'''
n, m = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))

l.sort()
# print('l[0]', l[0])
def find(l, first, last, m):
    cnt = 2
    result = 0
    l = set(l)
    while last >= first:
        mid = (first + last) // 2
        if mid in l:
            cnt += 1
        else:
            first = mid + 1

print(find(l, 0, len(l) - 1, m))