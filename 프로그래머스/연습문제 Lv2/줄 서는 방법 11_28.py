import math

def solution(n, k):
    answer = []
    dp = [0] * 1000

    dp[0] = 1
    dp[1] = 1
    k -= 1
    l = [i for i in range(1, n + 1)]

    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]

    while l:
        a = k // dp[n - 1]
        answer.append(l[a])
        del l[a]
        k = k % dp[n - 1]
        n -= 1

    return answer