from collections import deque


def solution(gems):
    if len(gems) == 1:
        return [1, 1]

    answer = deque([])

    t_answer = []

    lt, rt = 0, 0

    total_gems = len(set(gems))
    n = len(gems)

    gems_di = {}

    for i in gems:
        if i not in gems_di.keys():
            gems_di[i] = 0

    check = 0

    flag = False
    min_len = float('inf')

    while True:
        if lt == n or rt == n:
            break

        while rt < n:

            if check == total_gems:
                flag = True
                break

            if gems_di[gems[rt]] == 0:
                check += 1

            gems_di[gems[rt]] += 1

            rt += 1

        while lt < n:
            if check < total_gems:
                break

            gems_di[gems[lt]] -= 1

            if gems_di[gems[lt]] == 0:
                check -= 1

            lt += 1

        if rt - lt + 1 < total_gems:
            continue

        t_answer.append((lt, rt, rt - lt + 1))

    t_answer.sort(key=lambda o: (o[2], o[0]))
    #     print(t_answer)

    return [t_answer[0][0], t_answer[0][1]]