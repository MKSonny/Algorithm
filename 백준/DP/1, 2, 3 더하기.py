m = int(input())
l = []
for _ in range(m):
    l.append(int(input()))

n = 11

dp = [0 for _ in range(11 + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, n + 1):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for v in l:
    print(dp[v])