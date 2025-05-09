def solution(user_id, banned_id):
    answer = 0

    temp = [[] for _ in range(len(banned_id))]
    case = [[] for _ in range(len(banned_id))]

    for b in range(len(banned_id)):
        l = list(banned_id[b])
        temp[b].append(l)

        stars = []

        for i in range(len(l)):
            if l[i] == '*':
                stars.append(i)

        temp[b].append(stars)

    t_idx = 0
    for a, stars in temp:
        for i in user_id:
            if len(a) != len(i):
                continue

            l = list(i)

            for idx in stars:
                l[idx] = '*'

            if l == a:
                case[t_idx].append(i)

        t_idx += 1

    answer = []
    # s = []

    di = {}

    for i in case:
        for j in i:
            if j not in di.keys():
                di[j] = False

    t_a = []

    def dfs(level, s):
        if level == len(case):
            # print(s)
            t_a.append(set(s[:]))
            return

        for i in range(len(case[level])):
            if case[level][i] in s: continue
            # if case[level][i] in s: continue
            s.append(case[level][i])

            dfs(level + 1, s)
            s.pop()

    dfs(0, [])

    answer = set()

    for i in t_a:
        answer.add(frozenset(i))

    return len(answer)