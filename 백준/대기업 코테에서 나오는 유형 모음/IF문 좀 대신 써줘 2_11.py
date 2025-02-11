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

for _ in range(m):
    sc.append(int(sys.stdin.readline()))

idx = 0
ans = []

for i in sc:
    if int(lo[idx][1]) < i:
        idx += 1
        if idx == len(lo): break
    ans.append(lo[idx][0])

n = len(lo)

if len(ans) != m:
    for _ in range(m - len(ans)):
        ans.append(lo[n - 1][0])

for i in ans: print(i)