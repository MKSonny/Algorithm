import sys

n = int(sys.stdin.readline())
lo = []
for _ in range(n):
    lo.append(list(map(int, sys.stdin.readline().split())))

dp = [-1] * 31
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 31):
    dp[i] = i * dp[i - 1]


for a, b in lo:
    print(dp[b] // (dp[a] * dp[b - a]))