def solution(n):
    answer = 0

    dp = [0 for _ in range(2002)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    if n > 2:
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n] % 1234567