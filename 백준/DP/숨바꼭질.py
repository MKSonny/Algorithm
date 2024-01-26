n, k = map(int, input().split())

dp = [float("inf") for _ in range(300001)]
dp[n] = 0

for i in range(n):
    dp[i] = n - i

for i in range(n + 1, k + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
    else:
        dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 2)

print(dp[k])