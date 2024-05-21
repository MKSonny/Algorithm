final = 1
toggle = 1

def solution(n):
    answer = [[] for _ in range(n + 1)]

    def dfs(level, answer):
        global final
        global cnt
        print(answer)
        cnt += 1
        if level == n:
            for i in range(level):
                answer[level].append(final)
                final += 1
            return

        answer[level].append(final)
        final += 1
        dfs(level + toggle, answer)

    dfs(1, answer)
    print(answer)

    return answer

solution(4)