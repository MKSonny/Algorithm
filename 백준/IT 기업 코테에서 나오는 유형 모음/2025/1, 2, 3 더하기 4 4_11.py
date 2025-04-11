import sys

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    print(dp[m])