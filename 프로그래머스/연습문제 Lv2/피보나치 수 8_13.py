def solution(n):
    dp = [0] * 100001

    dp[0] = 0
    dp[1] = 1

    i = 2

    while True:
        dp[i] = dp[i - 1] + dp[i - 2]
        if i == n:
            return dp[i] % 1234567
        i += 1