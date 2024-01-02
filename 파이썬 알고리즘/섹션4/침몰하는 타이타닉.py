n, m = map(int, input().split())
l = list(map(int, input().split()))

'''
5 140
90 50 70 100 60
'''

l.sort()

# print(l)
cnt = 0

while l:
    # print(l)
    if l[0] + l[len(l) - 1] > m:
        l.pop()
        cnt += 1
    elif len(l) == 1:
        l.pop()
        cnt += 1
    else:
        l.pop()
        l.pop(0)
        cnt += 1

print(cnt)