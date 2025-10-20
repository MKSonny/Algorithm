def solution(land):
    answer = 0

    n = len(land)

    dp = [[0 for _ in range(4)] for _ in range(n)]

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, n):
        for c in range(4):
            for m in range(4):
                if c != m:
                    dp[i][c] = max(dp[i - 1][m] + land[i][c], dp[i][c])

    return max(dp[-1])