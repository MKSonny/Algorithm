answer = set()


def solution(numbers):
    l = list(numbers)
    n = len(l)

    def check(num):
        if num == 0 or num == 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def dfs(level, temp, visited):
        global answer

        if temp:
            t = ''.join(temp)
            answer.add(int(t))

        if level == n:
            return
        for i in range(n):
            if not visited[i]:
                temp.append(l[i])
                visited[i] = True
                dfs(level + 1, temp, visited)
                visited[i] = False
                temp.pop()

    visited = [False for _ in range(n)]
    dfs(0, [], visited)

    an = list(answer)
    cnt = 0

    for i in an:
        if check(i):
            cnt += 1
    # print(an)

    return cnt