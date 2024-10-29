def solution(skill, skill_trees):
    answer = 0

    d = {}
    cnt = 0

    for i in skill:
        d[i] = cnt
        cnt += 1

    def check(t):
        latest = 'a'
        b = True
        for i in t:
            if i in d:
                # print(latest, d[i], i)
                if latest == 'a':
                    if d[i] != 0:
                        b = False
                        return b
                else:
                    if latest != d[i] - 1:
                        b = False
                        return b
                latest = d[i]

        return b

    for i in skill_trees:
        # print(i, check(i))
        if check(i):
            answer += 1

    return answer