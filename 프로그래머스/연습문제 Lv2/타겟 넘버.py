cnt = 0

def solution(numbers, target):
    answer = 0

    total = len(numbers)
    numbers_minus = [-i for i in numbers]
    visited = [False] * total
    visited_minus = [False] * total
    sol = [0] * total

    def dfs(level, l, l_minus, n, sol, visited, visited_minus):
        global cnt
        if level == n:
            # print(sol)
            if sum(sol) == target:
                cnt += 1
            return

        if not visited[level]:
            sol[level] = l[level]
            visited[level] = True
            dfs(level + 1, l, l_minus, n, sol, visited, visited_minus)
            visited[level] = False

        if not visited_minus[level]:
            sol[level] = l_minus[level]
            visited_minus[level] = True
            dfs(level + 1, l, l_minus, n, sol, visited, visited_minus)
            visited_minus[level] = False

    dfs(0, numbers, numbers_minus, len(numbers), sol, visited, visited_minus)
    return answer