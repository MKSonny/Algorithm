n, W = map(int, input().split())
wt = []
val = []

for _ in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

print(wt)
print(val)

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, W + 1):
        if wt[i - 1] > w:
            dp[i][w] = dp[i - 1][w]
        else:
            valWith = val[i - 1] + dp[i - 1][w - wt[i - 1]]
            valWithout = dp[i - 1][w]
            dp[i][w] = max(valWith, valWithout)
'''
4 11
5 12
3 8
6 14
4 8
'''

for i in dp:
    print(i)
