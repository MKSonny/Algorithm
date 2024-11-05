def solution(arr):
    answer = [0, 0]
    l = len(arr)

    def dp(a, b, l):
        start = arr[a][b]
        for i in range(a, a + l):
            for j in range(b, b + l):
                if arr[i][j] != start:
                    l //= 2
                    dp(a, b, l)
                    dp(a + l, b, l)
                    dp(a, b + l, l)
                    dp(a + l, b + l, l)
                    return
        answer[start] += 1

    dp(0, 0, l)

    return answer