n, m = map(int, input().split())
l = list(map(int, input().split()))
'''
10 3
13 15 34 23 45 65 33 11 26 42
'''
l.sort(reverse=True)
cnt = 0
tmp = -1

h = []

for i in range(1, n - 1):
    sum = 0
    sum += l[i - 1] + l[i]
    for j in range(2, n):
        sum += l[j]
        print(sum)
        h.append(sum)
        sum -= l[j]


h.sort()
h = list(set(h))
h.sort()
print(h)
print(h[-m])