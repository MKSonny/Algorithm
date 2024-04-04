import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n + 1)]

if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + 1
    # 2랑 3 모두 나누어 떨어질 수 있기 때문에 elif 문 사용시 오답
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[n])