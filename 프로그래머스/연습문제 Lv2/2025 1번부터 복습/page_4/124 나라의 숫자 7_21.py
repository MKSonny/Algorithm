answer = ''


def solution(n):
    l = [1, 2, 4]

    def dfs(n):
        global answer
        # print('n', n)

        if n == -1:
            return

        # print(l[n % 3], end='')
        answer = str(l[n % 3]) + answer

        dfs((n // 3) - 1)

    dfs(n - 1)

    return answer