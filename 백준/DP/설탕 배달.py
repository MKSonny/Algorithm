n = int(input())

dp = [0 for _ in range(n + 1)]
dp[0] = -1

for w in range(1, n + 1):
    if w % 3 != 0:
        dp[w] = -1
        continue
    dp[w] = w // 3

if n > 4:
    dp[5] = 1

for w in range(8, n + 1):
    if dp[w] == -1:
        dp[w] = dp[w - 5] + 1
    elif dp[w - 5] == -1:
        continue
    else:
        dp[w] = min(dp[w], dp[w - 5] + 1)

print(dp[n])