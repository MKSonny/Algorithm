import sys

n = int(sys.stdin.readline())
l = [0] * 10000
for i in range(n):
    l[i] = int(sys.stdin.readline())

dp = [0] * 10000
dp[0] = l[0]
dp[1] = l[0] + l[1]
dp[2] = max(l[2] + l[1], l[2] + l[0], dp[1])

for i in range(3, n):
    dp[i] = max(l[i] + dp[i - 2], l[i] + l[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))