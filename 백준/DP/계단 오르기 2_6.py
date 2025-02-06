import sys

# n = int(sys.stdin.readline())
# lo = [0]
#
# for _ in range(n):
#     lo.append(int(sys.stdin.readline()))
#
# print(lo)

dp = [-1] * 301
# 마지막 계단은 무조건 밟아야 됨
# dp와 lo 점수가 동적임
# lo[i]

# 계단 2개
# lo[i - 1] + lo[i]

# 계단 3개
# max(lo[i - 2], lo[i - 1]) + lo[i]
# 3개일 경우 dp[i - 1]일 경우 3개를 연속해서 밟을 수 있음
# dp[1] = lo[1]
#
# dp[2] = lo[1] + lo[2]
#
# dp[3] = max(lo[1] + lo[3], lo[2] + lo[3])

# dp[4] = lo[1] + lo[2] + lo[4]
# dp[4] = lo[1] + lo[3] + lo[4]
#
# dp[4] = dp[2] + lo[4]
# dp[4] = dp[3] + lo[4]

# dp[3] = 1, 3
# dp[3] = 2, 3

# dp[4] = 1, 2, 4
# dp[4] = 1, 3, 4

# dp[5] = 1, 2, 4, 5
# dp[5] = 1, 3, 5
# dp[5] = 2, 3, 5

def dfs(level, cnt):
    if level <= 0:
        print()
        return
    print(level, cnt)
    if cnt < 1:
        dfs(level - 1, cnt + 1)
    dfs(level - 2, 0)

dfs(5, 0)

# for i in range(4, n + 1):
#     dp[i - 1] ==
#     dp[i] = max(dp[i - 2], dp[i - 1]) + lo[i]