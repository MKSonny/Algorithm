n = int(input())
l = list(map(int, input().split()))
'''
10 
45 73 66 87 92 67 75 79 75 80
'''
base = round(sum(l) / n)
h = []
for value in l:
    h.append(abs(value - base))

dis = min(h)
tmp = []
for i in range(n):
    if dis == h[i]:
        tmp.append((i + 1, l[i]))

# print(tmp)
maxx = max(tmp, key=lambda o:o[1])
# print(maxx[1])
for i in tmp:
    if i[1] == maxx[1]:
        print(base, i[0])
        break