import sys

n = int(sys.stdin.readline())

lo = list(map(int, sys.stdin.readline().split()))

dp = [min(lo)] * n
print(dp)

for i in range(n):
    to = 0
    for j in range(i, -1, -1):
        to += lo[j]
        dp[i] = max(dp[i], to)

print(dp)