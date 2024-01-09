n, m = map(int, input().split())

l = []

for _ in range(n):
    wt, val = map(int, input().split())
    l.append((wt, val))

dp = [0] * (m + 1)

for wt, val in l:
    for w in range(1, m + 1):
        if wt <= w:
            dp[w] = max(dp[w - wt] + val, dp[w])

print(dp[m])