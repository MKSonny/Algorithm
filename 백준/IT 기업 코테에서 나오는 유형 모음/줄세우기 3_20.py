import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

dp = [1] * n

for i in range(n):
    max_dp = -1
    for j in range(i):
        if l[i] > l[j]:
            max_dp = max(dp[j] + 1, max_dp)
            dp[i] = max_dp

print(n - max(dp))