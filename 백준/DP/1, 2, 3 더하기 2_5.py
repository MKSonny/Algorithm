import sys

n = int(sys.stdin.readline())
lo = []

for _ in range(n):
    lo.append(int(sys.stdin.readline()))

dp = [-1] * 13
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

'''
2
1 + 1
2

3
1 + 2
2 + 1
1 + 1 + 1

dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
'''
for i in range(5, 13):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for i in lo:
    print(dp[i])