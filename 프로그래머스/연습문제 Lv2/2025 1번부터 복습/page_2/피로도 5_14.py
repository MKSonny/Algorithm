answer = 0


def solution(k, dungeons):
    def check(l, k):
        cnt = 0

        for minimum, minus_k in l:
            if k >= minimum:
                k -= minus_k
                cnt += 1
                continue
            return cnt

        return cnt

    def dfs(level, temp, visited, k):
        global answer

        if level == len(dungeons):
            answer = max(answer, check(temp, k))
            return

        for i in range(len(dungeons)):
            if not visited[i]:
                temp.append(dungeons[i])
                visited[i] = True
                dfs(level + 1, temp, visited, k)
                temp.pop()
                visited[i] = False

    visited = [False for _ in range(len(dungeons))]
    dfs(0, [], visited, k)

    return answer