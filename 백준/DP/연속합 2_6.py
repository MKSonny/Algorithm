import sys

n = int(sys.stdin.readline())

lo = list(map(int, sys.stdin.readline().split()))

maxx = -1
total = 0
al = sum(lo)
# print(al)

for j in range(n - 1, 0, -1):
    al -= lo[j]
    total = al
    # print('st', total)
    for i in range(n - j):
        total -= lo[i]
        total += lo[i + j]
        maxx = max(maxx, total)
        # print(total)
    # print()

# for j in range(1, n):
#     # total = sum(lo[: + j])
#     # maxx = max(maxx, total)
#     for i in range(n - j):
#         total -= lo[i]
#         total += lo[i + j]
#         maxx = max(maxx, total)
#         print(total)
#     print()

print(maxx)
# l[0] + l[1] + l[2]
# total = l[0] + l[1] + l[2]

# total -= l[0]
# total += l[3]
# l[1] + l[2] + l[3]

# l[0] + l[1] + l[2] + l[3]
# l[1] + l[2] + l[3] + l[4]
