import sys

n, k = map(int, sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1


for coin in arr:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]


print(dp[k])