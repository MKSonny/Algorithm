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
    while last >= first:
        mid = (first + last) // 2
        cnt += 1
        print(first, last, mid, cnt)
        if first == mid or last == mid:

        if cnt == m:
            # print(mid, first, last)
            # print(l[mid], l[first], l[last])
            return min(abs(l[mid] - l[first]), abs(l[mid] - l[last]))
        if abs(l[mid] - l[first]) < abs(l[mid] - l[last]):
            first = mid
        else:
            last = mid
    return result

print(find(l, 0, len(l) - 1, m))