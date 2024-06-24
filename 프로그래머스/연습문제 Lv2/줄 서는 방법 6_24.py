cnt = 0


def permutations(level, n, l, sol, visited, k):
    global cnt
    if level == n and cnt == k - 1:
        return sol
    if level == n:
        cnt += 1
        return
    for i in range(n):
        if not visited[i] and cnt < k:
            sol.append(l[i])
            visited[i] = True
            if permutations(level + 1, n, l, sol, visited, k):
                return sol
            visited[i] = False
            sol.pop()


def solution(n, k):
    l = [i for i in range(1, n + 1)]
    visited = [False] * n
    k = 3

    return permutations(0, n, l, [], visited, k)