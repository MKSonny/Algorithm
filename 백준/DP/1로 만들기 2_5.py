import sys

n = int(sys.stdin.readline())

dp = [-1] * (10**6 + 1)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    a, b = dp[i], dp[i]
    if i % 2 == 0 and dp[i // 2] != -1:
        a = dp[i // 2]

    if i % 3 == 0 and dp[i // 3] != -1:
        b = dp[i // 3]

    if a < 0 and b < 0:
        dp[i] = dp[i - 1] + 1
    elif a > 0 and b > 0:
        dp[i] = min(a, b) + 1
    elif a > 0 and b == -1:
        dp[i] = min(a + 1, dp[i - 1] + 1)
    elif a == -1 and b > 0:
        dp[i] = min(b + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i - 1] + 1

print(dp[n])
