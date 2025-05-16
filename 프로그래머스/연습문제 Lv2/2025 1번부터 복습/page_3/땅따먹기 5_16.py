maxx = -1


def solution(land):
    answer = 0

    dp = [[0 for _ in range(4)] for _ in range(len(land))]


    for i in range(4):
        dp[0][i] = land[0][i]

    for m in range(1, len(land)):
        for i in range(4):
            for j in range(4):
                if j != i:
                    dp[m][j] = max(dp[m][j], dp[m - 1][i] + land[m][j])

    #     for i in dp:
    #         print(i)

    return max(dp[-1])