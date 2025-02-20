import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)

total = sum(li)
dp[n] = total
# print(sum(li))

for i in range(n - 1, -1, -1):
    total -= li[i]
    dp[i] = total

# print(dp)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[end] - dp[start - 1])