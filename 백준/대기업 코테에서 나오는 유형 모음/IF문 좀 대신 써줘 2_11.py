import sys

n, m = map(int, sys.stdin.readline().split())
lo = []
sc = []
test = []
idx = 0
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    # print(idx, a, b)
    if idx > 0 and lo[idx - 1][1] == int(b):
        # print(a, lo[idx - 1][1], b)
        continue
    idx += 1
    lo.append((a, int(b)))

n = len(lo)
# print(lo)

for i in range(m):
    sc.append(((int(sys.stdin.readline())), i))

sc.sort()
k = 0
ans = []

'''
3 8
WEAK 10000
NORMAL 10000
STRONG 1000000
0
9999
10000
10001
50000
100000
500000
1000000
===========

3 5
B 100
A 101
C 102
99
100
101
500
1000
'''

for i, idx in sc:
    if int(lo[k][1]) < i:
        k += 1
        if k == len(lo):
            k = len(lo) - 1
    ans.append((idx, lo[k][0]))

ans.sort()
for a, b in ans:
    print(b)
# n = len(lo)
#
# if len(ans) != m:
#     for _ in range(m - len(ans)):
#         ans.append(lo[n - 1][0])
#
# for i in ans: print(i)