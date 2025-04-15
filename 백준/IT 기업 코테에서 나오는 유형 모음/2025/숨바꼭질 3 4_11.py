import sys

dp = [0] * 100001
n, m = map(int, sys.stdin.readline().split())

idx = n
while idx > 0:
    if dp[idx - 1] > 0:
        dp[idx - 1] = min(dp[idx - 1], dp[idx] + 1)
    else:
        dp[idx - 1] = dp[idx] + 1

    idx -= 1

idx = n
while idx < m + 1:
    if dp[idx + 1] > 0:
        dp[idx + 1] = min(dp[idx + 1], dp[idx] + 1)
    else:
        dp[idx + 1] = dp[idx] + 1

    idx += 1



print(dp)