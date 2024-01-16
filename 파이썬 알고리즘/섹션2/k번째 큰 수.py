n, m = map(int, input().split())
l = list(map(int, input().split()))
'''
10 3
13 15 34 23 45 65 33 11 26 42
'''
cnt = 0
tmp = -1

h = []

# for i in range(n):
#     sum = 0
#     sum += l[i]
#     for j in range(i + 1, n):
#         sum += l[j]
#         for k in range(j + 1, n):
#             sum += l[k]
#             h.append(sum)
#             sum -= l[k]
#         sum -= l[j]
#     sum -= l[i]

res = set()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            res.add(l[i] + l[j] + l[k])

# h.sort()
# h = list(set(h))
# h.sort()

res = list(res)
res.sort()

# print(h)
print(res[-m])