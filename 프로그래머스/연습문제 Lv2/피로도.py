max_dun = -1


def solution(k, dungeons):
    answer = -1

    a = k

    def is_safe(a, sol):
        cnt = 0
        for i in sol:
            if i[0] <= a:
                a -= i[1]
                cnt += 1
        return cnt

    def permutation(level, l, sol, visited, k):
        global max_dun
        if level == k:
            max_dun = max(is_safe(a, sol), max_dun)
            return
        for i in range(len(l)):
            if not visited[i]:
                sol.append(l[i])
                visited[i] = True
                permutation(level + 1, l, sol, visited, k)
                sol.pop()
                visited[i] = False

    n = len(dungeons)
    v = [False] * n
    permutation(0, dungeons, [], v, n)

    return max_dun