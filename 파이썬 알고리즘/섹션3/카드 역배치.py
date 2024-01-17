l = [i + 1 for i in range(20)]

def _do(l, n, m):
    n -= 1
    m -= 1
    for i in range(abs(n - m) // 2 + 1):
        # tmp = l[n + i]
        # l[n + i] = l[m - i]
        # l[m - i] = tmp
        l[n + i], l[m - i] = l[m - i], l[n + i]

for _ in range(10):
    n, m = map(int, input().split())
    _do(l, n, m)

for i in l:
    print(i, end=' ')