n, m = map(int, input().split())
h = [0 for _ in range(n + m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        h[i + j] += 1

maxx = max(h)
for i in range(n + m + 1):
    if h[i] == maxx:
        print(i, end=' ')