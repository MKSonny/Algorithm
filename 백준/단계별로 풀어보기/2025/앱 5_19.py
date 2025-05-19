import sys

n, m = map(int, sys.stdin.readline().split())

memory_list = [0] + list(map(int, sys.stdin.readline().split()))
cost_list = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(sum(cost_list) + 1)] for _ in range(n + 1)]

answer = sum(cost_list)

for i in range(1, n + 1):
    for j in range(sum(cost_list) + 1):
        dp[i][j] = dp[i - 1][j]

    for j in range(cost_list[i], sum(cost_list) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost_list[i]] + memory_list[i])
        if dp[i][j] >= m:
            answer = min(answer, j)

    for i in dp:
        print(i)
    print()

# for i in dp:
#     print(i)
print(answer)