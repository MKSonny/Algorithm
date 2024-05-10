answer = 0


def solution(m, n, board):
    stack = [[] for _ in range(n)]

    for i in range(m - 1, -1, -1):
        for j in range(n):
            stack[j].append(board[i][j])

    answer = 0

    while True:
        where_to_pop = set()

        for i in range(len(stack) - 1):
            n = len(stack[i])
            for key in range(n - 1, 0, -1):
                if len(stack[i + 1]) - 1 < key:
                    continue
                if stack[i][key] == stack[i + 1][key] == stack[i + 1][key - 1] == stack[i][key - 1]:
                    where_to_pop.add((i, key))
                    where_to_pop.add((i + 1, key))
                    where_to_pop.add((i + 1, key - 1))
                    where_to_pop.add((i, key - 1))

        if len(where_to_pop) == 0:
            break
        where_to_pop = sorted(list(where_to_pop))

        while where_to_pop:
            y, x = where_to_pop.pop()
            answer += 1
            stack[y].pop(x)

    return answer