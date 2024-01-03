n = int(input())

l = list(map(int, input().split()))

'''
5
2 4 5 1 3

10
3 2 10 1 5 4 7 8 9 6
'''
rt = 0
h = []
an = []

while l:
    if rt < l[0]:
        if rt < l[-1]:
            if l[0] < l[-1]:
                rt = l.pop(0)
                h.append(rt)
                an.append('L')
            else:
                rt = l.pop()
                h.append(rt)
                an.append('R')
        else:
            rt = l.pop(0)
            h.append(rt)
            an.append('L')
    else:
        if rt < l[-1]:
            rt = l.pop()
            h.append(rt)
            an.append('R')
        else:
            break

print(len(h))
for k in an:
    print(k, end='')